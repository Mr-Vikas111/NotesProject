from django.urls import path
from .views import UserSignup,UserLogin,UserLogout,UserProfile
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('register/',csrf_exempt(UserSignup),name='regiter'),
    path('login/',UserLogin,name='login'),
    path('logout/',UserLogout,name='logout'),
    path('profile/',UserProfile,name='profile'),
    
]