from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import sign_up_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# usercreationform is used to sign up or create user.


def sign_up(request):
    if request.method == 'POST':
        fm = sign_up_form(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.success()
    else:
        fm = sign_up_form()
    return render(request, 'Sign-up.html', context={'fm': fm})

# Authentication form is used to login.


def login_user(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user_cr = authenticate(username=uname, password=upass)
            if user_cr is not None:
                login(request, user_cr)
                return redirect('home')
    else:
        fm = AuthenticationForm()
    return render(request, 'sign-in.html', context={'fm': fm})
