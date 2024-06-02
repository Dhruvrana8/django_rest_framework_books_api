from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=250)
    author=models.CharField(max_length=100)
    create_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

