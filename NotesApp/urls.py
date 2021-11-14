from django.urls import path
from .views import NotesListView,NotesDetailView
urlpatterns = [
    path('notes/',NotesListView.as_view(),name="notesdata"),
    path('notes/<int:pk>/',NotesDetailView.as_view(),name="getnotedata")
]