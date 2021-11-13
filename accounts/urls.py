from django.urls import path
from .views import UserRegisterView,MyObtainTokenPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt



urlpatterns =[
    path('register/',csrf_exempt(UserRegisterView.as_view()),name="userregister"),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
]