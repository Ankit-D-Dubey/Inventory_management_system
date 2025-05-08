from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='user-login')
def index(request):
    orders=Order.objects.all()
    orders_count=Order.objects.all().count()
    products= Product.objects.all()
    workers_count=User.objects.all().count()
    product_count=Product.objects.all().count()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff=request.user            
            # instance.save()
            product = instance.product 
            if instance.order_quantity > product.quantity:
                messages.error(request,"Insufficient stock ! Only {} available".format(product.quantity))
            else:
                instance.save()
                product.quantity -= instance.order_quantity
                product.save()
                messages.success(request,f"Order placed successfully ! {instance.order_quantity} items sold. ")
                return redirect("dashboard-index")
    else:
        form=OrderForm()
    products=Product.objects.all()
    context = {
        'orders_count':orders_count,
        'products':products,
        'orders':orders,
        'form':form,
        'workers_count':workers_count,
        'product_count':product_count,
        
    }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='user-login')
def staff(request):
    workers=User.objects.all()
    workers_count=User.objects.all().count()
    orders_count=Order.objects.all().count()
    product_count=Product.objects.all().count()
    context={
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id=pk) 
    context={
        'workers':workers,
        
    }
    return render(request,"dashboard/staff_detail.html",context)

@login_required(login_url='user-login')
def product(request):
    workers_count=User.objects.all().count()
    orders_count=Order.objects.all().count()
    product_count=Product.objects.all().count()
    items=Product.objects.all()
    order=Order.objects.all()
    if request.GET.get('search'):
        items = items.filter(name__icontains = request.GET.get('search'))
    #items=Product.objects.raw("select * from dashboard_product") same as .all()
    if request.method=="POST":
        form =ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form=ProductForm()
    context = {
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count,
        
    }
    return render(request,'dashboard/product.html',context)

@login_required(login_url='user-login')
def add_product(request):
    workers_count=User.objects.all().count()
    orders_count=Order.objects.all().count()
    product_count=Product.objects.all().count()
    if request.method=="POST":
        add_form=ProductForm(data=request.POST)
        if add_form.is_valid():
            new_inventory=add_form.save(commit=False)
            new_inventory.sales=float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            
            new_inventory.save()
            product_name = add_form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added successfully ! ')
            return redirect("/product")
    else:
        add_form=ProductForm()
        
    context = {
        
        'form':add_form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count
    }
    return render(request,'dashboard/add_product.html',context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method =="POST":
        item.delete()
        messages.error(request,f'{item.name} has been deleted successfully !!')
        return redirect("dashboard-product")
    return render(request,'dashboard/product_delete.html',{'item':item})

@login_required
def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method== "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            item.name=form.data['name']
            item.quantity=form.data['quantity']
            item.quantity_sold=form.data['quantity_sold']
            item.cost_per_item=form.data['cost_per_item']
            item.sales=float(item.cost_per_item) * float(item.quantity_sold)
            item.save()
            return redirect("/product")
                  
    else:
        form =ProductForm(instance=item)
        
    context={
        'form':form
    }
    return render(request,'dashboard/product_update.html',context)

@login_required(login_url='user-login')
def per_product_view(request,pk):
    inventory=get_object_or_404(Product,pk=pk)
    
    context={
        'inventory':inventory
    }
    return render(request,"dashboard/per_product.html",context=context)

@login_required
def order(request):
    orders=Order.objects.all()
    orders_count=Order.objects.all().count()
    workers_count=User.objects.all().count()
    product_count=Product.objects.all().count()
    context={
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count
    }
    return render(request,"dashboard/order.html",context)

# @login_required
# def dashboard(request):
#     inventories=Product.objects.all()
#     df=read_frame(inventories)
#     sales_graph=df.groupby(by="last_sales_date",as_index=False,sort=False)['sales'].sum()