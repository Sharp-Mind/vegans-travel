from ast import mod
from venv import create
from django.db import models
from datetime import datetime 

class Posts(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    picture = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)