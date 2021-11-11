from django.contrib import admin
from .models import NotesModel
# Register your models here.

@admin.register(NotesModel)

class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','title','body','image','date','user']