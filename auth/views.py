from django.shortcuts import render
from django.contrib import messages
from models import User;
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def login_page(request):
    if request.method=="POST":
         email=request.POST.get('username')
         password=request.POST.get('password')
         if not User.objects().filter(email=email).exists():
              messages.error(request,'invalid email')
              return  redirect('/login/')
         user=authenticate(email=email,password=password)  
         print(user)
         if user is not None:
              login(request,user)
              return redirect('/dashboard/')
         else:
              messages.error(request,'invalid credentials')
              return  redirect('/login/')