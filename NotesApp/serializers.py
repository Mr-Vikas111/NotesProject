from rest_framework import serializers
from django.contrib.auth.models import User
from .models import NotesModel

class NoteSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = NotesModel
        fields = ['title','body','image','user']