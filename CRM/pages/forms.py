from .models import Customer,CustomerService,Service
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CreateCustomer(forms.ModelForm):
    class Meta:
        model= Customer
        fields=['name','email','address']

class UpdateCustomer(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','email','address']

class addServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.filter(is_active=True), label="Add service",
    widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model=CustomerService
        fields = ['service']

class loginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)