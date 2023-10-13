from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # for i in request.session:
    #     print(i)
    request.session['sample'] = ['sample data']
    request.session['sample'].insert(0,'zero data')
    print(vars(request.session))
    return HttpResponse("Hello")
