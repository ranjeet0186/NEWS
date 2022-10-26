from django.contrib.auth.models import User
from django.db import models

class Contact_Us(models.Model):    
    Name = models.CharField(max_length=100) 
    email=models.EmailField()
    mobile = models.CharField(max_length=10)    
    messages=models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
    

