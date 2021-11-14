from django.shortcuts import render, HttpResponseRedirect,redirect

def UserSignup(request):
    return render(request, 'webapp/signup.html')


def UserLogin(request):
    return render(request, 'webapp/userlogin.html')


def UserProfile(request):
    return render(request, 'webapp/profile.html')

def UserNote(request):
    return render(request, 'webapp/addnote.html')


def UserLogout(request):
    return HttpResponseRedirect('/userlogin')
