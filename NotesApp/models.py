from django.db import models
from django.contrib.auth.models import User

class NotesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title