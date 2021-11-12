from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import signupform, loginform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def UserSignup(request):
    if request.method == "POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account Created Successfully')

    else:
        fm = signupform()
    return render(request, 'webapp/signup.html', {'form': fm})


def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = loginform(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged successful')
                    return redirect('profile/')
        else:
            fm = loginform()
        return render(request, 'webapp/userlogin.html', {'form': fm})


def profile(request):
    return render(request, 'webapp/profile.html')


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/userlogin')
