from django.urls import path
from .views import UserSignup,UserLogin,UserLogout,UserProfile
urlpatterns=[
    path('register/',UserSignup,name='regiter'),
    path('login/',UserLogin,name='login'),
    path('logout/',UserLogout,name='logout'),
    path('profile/',UserProfile,name='profile')

    
]