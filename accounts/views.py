from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from . forms import SignupForm
from . models import Customer


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

    return render(request,'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            customer = Customer.objects.create(user=user,is_seller = form.cleaned_data['is_seller'])
            customer.save()
            return redirect('login')
        else:
            print("Something went wrong\n\n")
    else:
        form = SignupForm()
               
    return render(request,'signup.html',{'form':form})

def logout_view(request):
        logout(request)
        return redirect('/')
