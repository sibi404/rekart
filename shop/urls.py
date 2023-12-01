from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('addItem/',views.add_item,name='add_item'),
    path('product_details/<slug:slug>/',views.product_view,name='product_details'),
    path('plastic_details/<slug:slug>/',views.plastic_view,name='plastic_details'),
    path('delete_product/<int:product_id>/',views.delete_product,name='delete_product'),
    path('delete_plastic/<int:plastic_id>/',views.delete_plastic,name='delete_plastic'),
    path('update_product/<int:product_id>/',views.update_product,name='update_product'),
    path('update_plastic/<int:plastic_id>/',views.update_plastic,name='update_plastic')
]