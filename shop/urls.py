from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('addItem/',views.add_item,name='add_item'),
    path('product_details/<int:product_id>/',views.product_view,name='product_details'),
    path('delete_product/<int:product_id>/',views.delete_product,name='delete_product'),
    path('update/<int:product_id>/',views.update_product,name='update_product')
]