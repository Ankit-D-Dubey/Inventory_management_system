from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.index,name='dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('staff/detail/<int:pk>',views.staff_detail,name='dashboard-staff-detail'),
    path('order/',views.order,name='dashboard-order'),
    path('product/',views.product,name='dashboard-product'),
    path("add_product/", views.add_product , name="add_product"),
    path("per-product/<int:pk>", views.per_product_view , name="per_product_view"),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
]
