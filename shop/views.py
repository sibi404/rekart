from django.shortcuts import render

def shop(request):
    data = request.GET.get('data')
    print("DATA FOUND \t",data)
    return render(request,'shop1.html')
