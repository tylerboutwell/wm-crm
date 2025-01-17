from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..models import Customer

def home(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('crm_app:home')
        else:
            messages.success(request, "There was an error logging in. Please try again...")
            return redirect('crm_app:home')
    else:
        return render(request, 'crm/home.html', {'customers':customers})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('crm_app:home')


