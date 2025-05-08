from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('Sports','Sports'),
    ('Furniture','Furniture'),
)

class Product(models.Model):
    name = models.CharField(max_length=100 ,null=True)
    category = models.CharField(max_length=20 , choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)
    cost_per_item = models.DecimalField(max_digits=19,decimal_places=2,null=True,blank=True)
    quantity_sold = models.IntegerField(null=True,blank=True)
    sales = models.DecimalField(max_digits=19,decimal_places=2,null=True,blank=True)
    stock_date = models.DateField(auto_now_add=True,null=True)
    last_sales_date=models.DateField(auto_now_add=True,null=True)
    
    
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural='Products'
    
class Order(models.Model):
    #foreign key provides a many to one rel and it target pri key of another model which means id col
    #it means one product can be order multiple times by the same user
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    #cascade=if any product will be deleted then offcource order will also deleted
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.product} ordered by {self.staff}' 
    class Meta:
        verbose_name_plural='Orders'