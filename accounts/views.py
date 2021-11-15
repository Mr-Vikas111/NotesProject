from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    


class UserRegisterView(GenericAPIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]

    @csrf_exempt
    def post(self, request, format=None):
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'status': 404, 'message': serializer.errors})

            serializer.save()
            return Response({'status':201,'message':'Created'})
        except Exception as e:
            print(e)
            return Response({'status': 404, 'error': 'Something went Wrong'})
    
