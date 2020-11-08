from django.shortcuts import render, redirect
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def my_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('index:home')
            else:
                messages.error(request,'username or password not correct')
                return redirect('index:login')
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})