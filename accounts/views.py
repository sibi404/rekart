from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import logout


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

    return render(request,'login.html')

def logout_view(request):
        logout(request)
        return redirect('login')
