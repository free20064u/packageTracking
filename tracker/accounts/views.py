from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserAdminCreationForm, LoginForm


def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully register')
            return redirect('register')
        else:
            messages.error(request, 'User not registered')
            return render(request, 'accounts/register.html', {'form': form}) 
        
    return render(request, 'accounts/register.html', {'form': form})


def signInView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully login')
            return redirect('home')
        else:
            form = LoginForm()
            messages.error(request, 'Login in not successful')
            return render(request, 'accounts/login.html', { 'form':form })
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', { 'form':form })
    


def signOutView(request):
    logout(request)
    messages.success(request, 'You have logged out')
    return redirect('home')