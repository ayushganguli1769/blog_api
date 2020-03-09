from django.shortcuts import render
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def home(request):
    return render(request,'home.html')
def add(request):
    return render(request,'add.html')
def base(request):
    return render(request,'base.html')