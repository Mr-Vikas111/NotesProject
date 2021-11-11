from rest_framework import serializers
from django.contrib.auth.models import User
from .models import NotesModel

class NoteSerializer(serializers.ModelSerializer):
    imagefield = serializers.ImageField()
    class Meta:
        model = NotesModel
        fields = ['title','body','imagefield','user']