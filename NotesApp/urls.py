from django.urls import path
from .views import NoteListView,NoteDetailView

urlpatterns = [
    path('notes/',NoteListView.as_view(),name="notesdata"),
    path('notes/<int:pk>',NoteDetailView.as_view(),name="getnotedata")
]