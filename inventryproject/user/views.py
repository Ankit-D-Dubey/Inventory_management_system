from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
def register(request):
    if request.method =="POST":
        form=CreateUserForm(request.POST) #jo collect kiya hai data vo form me store ho jayega
        if form.is_valid(): #default validations
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {user_name}. continue to login !!')
            return redirect('user-login')
    else:
        form=CreateUserForm()
        
    context={
        'form':form,
    }
    return render(request,'user/register.html',context)

@login_required(login_url='user-login')
def profile(request):
    # profile= Profile.objects.all()
    # user=User.objects.all()
    return render(request,'user/profile.html')

@login_required(login_url='user-login')
def profile_update(request):
    user =request.user
    if not hasattr(user,'profile'):
        Profile.objects.create(staff=user)
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("user-profile")
    else:
        user_form=UserUpdateForm(instance=user)
        profile_form=ProfileUpdateForm(instance=user.profile)
        
    return render(request,'user/profile_update.html',{'user_form':user_form,'profile_form':profile_form})

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)