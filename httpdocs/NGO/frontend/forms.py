from django import forms
from .models import*

class Contact_us_Form(forms.ModelForm):
    messages = forms.CharField(widget=forms.Textarea)  
    class Meta:
        model = Contact_Us
        fields = '__all__'  