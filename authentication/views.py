from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm


# Create your views here.

def register(request):
    user = request.user
    if not user.is_anonymous:
        return redirect('profile')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm(request.POST)

    return render(request, "auth/register.html", {'form': form})


def sign_in(request):
    user = request.user
    if not user.is_anonymous:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Wrong data")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')
