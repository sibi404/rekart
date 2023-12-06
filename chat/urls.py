from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('new/<int:plastic_id>/',views.new_conversation,name='new'),
    path('inbox/',views.inbox,name='inbox')
]