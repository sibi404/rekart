from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='cart_index'),
    path('delete/<int:product_id>/',views.delete_item,name='cart_item_delete')
]