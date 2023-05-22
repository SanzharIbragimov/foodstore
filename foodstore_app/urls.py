from django.contrib import admin
from django.urls import include, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('product/<int:id>/', get_description_by_id, name="product_description"),
    path('customers/', all_customers, name="all_customers"),
    path('customer/<int:id>/', customer_detail, name="customer_detail"),
    path('customer/create/', create_customer, name="create_customer"),
    path('customer/update/<int:id>/', update_customer, name="update_customer"),
    path('customer/delete/<int:id>/', delete_customer, name="delete_customer"),
    path('products/', product_list, name="product_list"),
    path('product/create/', create_product, name="create_product"),
    path('product/update/<int:id>/', update_product, name="update_product"),
    path('product/delete/<int:id>/', delete_product, name="delete_product"),
    path('', include('django.contrib.auth.urls')),
    path("register/", registerView.as_view(), name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
