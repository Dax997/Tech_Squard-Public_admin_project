from django.shortcuts import render, redirect
from . forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('homepage')
        else:
            messages.success(request, "Error! Authentication failed, check your username or password")
            return redirect('login')
    else:
        return render(request,'Members/login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            
            messages.success(request, "Registration successful, you are now logged in")
            return redirect('homepage')

    else:
        form = UserForm()
        return render(request,'Members/register.html', {'form':form})
    
def logout_user(request):
    logout(request)
    messages.success(request, "Singed out successfully")
    return redirect('homepage')