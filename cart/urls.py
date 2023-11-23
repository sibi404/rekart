from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.index,name='cart_index'),
    path('addCart/<int:product_id>/',views.add_to_cart,name='add_cart'),
    path('delete/<int:product_id>/',views.delete_item,name='cart_item_delete'),
    path('addCount/<int:product_id>/',views.add_count,name='add_count'),
    path('reduceCount/<int:product_id>/',views.reduce_count,name='reduce_count')
]