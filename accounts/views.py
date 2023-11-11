from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import logout


def login(request):
    if request.method == 'POST':
        print("Reached\n\n\n")
        email = request.POST['email']
        password = request.POST['password']

        # print("Email : ",email)
        # print("Password : ",password)

        user = authenticate(username=email,password = password)

        if user is not None:
            print("LOGIN\n\n")
            auth.login(request,user)
            return redirect('/')
        else:
            print("Error!!!!!")


    return render(request,'login.html')

def logout_view(request):
        logout(request)
        return redirect('/')
