
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.forms import fields, widgets
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import*



class ServicesForm(forms.ModelForm):  
    class Meta:
        model = Services
        fields = '__all__'  

class GalleryForm(forms.ModelForm):  
    class Meta:
        model = Gallaery
        fields = '__all__'  

class OurTeamForm(forms.ModelForm):  
    class Meta:
        model = OurTeam
        fields = '__all__'

class OurTestimonialForm(forms.ModelForm):  
    class Meta:
        model = OurTestimonial
        fields = '__all__' 

class OurPartnersForm(forms.ModelForm):  
    class Meta:
        model = OurPartners
        fields = '__all__' 

class DonateNowForm(forms.ModelForm):  
    class Meta:
        model =  DonateDetail
        fields = '__all__'         

class AdminProfileForm(UserChangeForm):
    password=None       
    class Meta():
        model = User
        fields = ['first_name','last_name','username','email']


class Admin_Profile_Pic_Form(forms.ModelForm):          
    class Meta():
        model = AdminProfile_Picture
        fields = ['image']
        exclude=['password']        
        
        

class UserForm(forms.ModelForm):    
    class Meta():
        model = User
        fields = ['first_name','last_name','username']
        
        
        
        
class UserProfileForm(forms.ModelForm):         
    class Meta():
        model = Members
        fields = ('mobile','image')
        


class Contact_Details_Form(forms.ModelForm):  
    class Meta:
        model = Contact_Deatails
        fields = '__all__' 

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_("Email"),max_length=255,widget=forms.EmailInput(attrs={'class':'form-control','autocomplete':'email'}))


class MySetPasswordForm(SetPasswordForm):   
   new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}),help_text=password_validation.password_validators_help_text_html()) 
   new_password2=forms.CharField( label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}))         

