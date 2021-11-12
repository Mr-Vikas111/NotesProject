from django.shortcuts import render
from .models import NotesModel
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import NoteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
# Create your views here.

class NoteListView(generics.ListCreateAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NoteSerializer
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        current_user = self.request.user
        queryset = NotesModel.objects.filter(user=current_user)
        return queryset
    

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NoteSerializer
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]