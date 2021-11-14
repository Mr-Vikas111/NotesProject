from rest_framework import serializers
from django.contrib.auth.models import User
from .models import NotesModel

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = '__all__'



class NoteSerializerForGetPut(serializers.ModelSerializer):
    
    class Meta:
        model=NotesModel
        fields=['title','body']