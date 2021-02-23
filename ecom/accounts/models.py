from django.db import models

# Create your models here.
class User(models.Model):
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
