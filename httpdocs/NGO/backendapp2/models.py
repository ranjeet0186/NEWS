from django.contrib.auth.models import User
from django.db import models


class Services(models.Model):    
    title = models.CharField(max_length=255) 
    description=models.TextField()
    image = models.ImageField(upload_to='media/services/images',default='static/frontend/images/1/jpg')
    is_home = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    

class Gallaery(models.Model):    
    title = models.CharField(max_length=255) 
    description=models.CharField(max_length=255)
    image = models.ImageField(upload_to='admin/gallery',default='static/frontend/images/1/jpg')
    is_home = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    

class OurTeam(models.Model):    
    Name = models.CharField(max_length=100) 
    mobile = models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/services/images',default='static/frontend/images/1/jpg')
    is_home = models.BooleanField(default=True)
    status = models.BooleanField(default=True)

class OurTestimonial(models.Model):    
    Name = models.CharField(max_length=100)      
    designation=models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/testimonial',default='static/frontend/images/1/jpg',null=True)
    description = models.TextField()
    is_home = models.BooleanField(default=True)
    status = models.BooleanField(default=True)  

class OurPartners(models.Model):    
    Name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='media/ourpartners',default='static/frontend/images/1/jpg',null=True)    
    is_home = models.BooleanField(default=True)
    status = models.BooleanField(default=True)    


class Members(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    mobile =models.CharField(max_length=10)
    image = models.ImageField(upload_to ='uploads/client/user',default='avtar.png', null=True,blank=True) 
    gender =models.CharField(max_length=15,null=True)
    address =models.CharField(max_length=100,null=True)
    status = models.BooleanField(default=True)    
    def __str__(self):
        return self.user.username
    


class DonateDetail(models.Model):
    user=models.ForeignKey(Members, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)

class AdminProfile_Picture(models.Model):
    image = models.ImageField(upload_to ='uploads/admin',default='avtar.png', null=True,blank=True)

class Contact_Deatails(models.Model):   
    mobile =models.CharField(max_length=15)
    email =models.EmailField(unique=True)
    address =models.CharField(max_length=214)


