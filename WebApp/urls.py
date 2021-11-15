from django.urls import path
from .views import UserSignup,UserLogin,UserLogout,UserProfile,UserNote
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('register/',UserSignup,name='regiter'),
    path('login/',UserLogin,name='login'),
    path('logout/',UserLogout,name='logout'),
    path('profile/',UserProfile,name='profile'),
    path('addnote/',UserNote,name='addnote'),
    
]