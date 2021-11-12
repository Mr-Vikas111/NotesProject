from django.urls import path
from .views import UserSignup,UserLogin,UserLogout
urlpatterns=[
    path('register/',UserSignup,name='regiteruser'),
    path('login/',UserLogin,name='loginuser'),
    path('logout/',UserLogout,name='logoutuser'),

    
]