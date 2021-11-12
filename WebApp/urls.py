from django.urls import path
from .views import UserSignup,UserLogin,UserLogout,UserProfile
urlpatterns=[
    path('register/',UserSignup,name='regiteruser'),
    path('login/',UserLogin,name='loginuser'),
    path('logout/',UserLogout,name='logoutuser'),
    path('profile/',UserProfile,name='profile')

    
]