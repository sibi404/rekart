from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . forms import LoginForm

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html',authentication_form = LoginForm),name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout')
]