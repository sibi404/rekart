from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('addItem/',views.add_item,name='add_item'),
]