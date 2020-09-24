from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Info(models.Model):
    objects = None
    place = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    
    def __str__(self):
        return self.email
