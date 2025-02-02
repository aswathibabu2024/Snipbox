from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Tag(models.Model):
    """ store titles for snippets """
    
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title




class Snippet(models.Model):
    """model for short text snippets"""
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

