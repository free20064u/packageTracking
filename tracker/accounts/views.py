from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserAdminCreationForm, LoginForm


def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(request, 'accounts/register.html', {'form': form})


def signInView(request):
    print("logogoingo")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = LoginForm()
            return render(request, 'accounts/login.html', { 'form':form })
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', { 'form':form })
    


def signOutView(request):
    logout(request)
    return redirect('home')