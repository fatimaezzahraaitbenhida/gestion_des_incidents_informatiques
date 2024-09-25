from django.core import validators
from django import forms
from django.forms import fields,widgets
from .models import CustomUser
from .models import Incident
class IncidentRegistration(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nom','prenom','email','mot_de_passe','service']
        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'mot_de_passe' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'service' : forms.TextInput(attrs={'class': 'form-control'}),
        }
class Incidenta(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['description','user','type']
        widgets = {
            'description' : forms.TextInput(attrs={'class': 'form-control'}),
            'user' : forms.EmailInput(attrs={'class': 'form-control'}),
            'type' : forms.TextInput(attrs={'class': 'form-control'}),
        }     
class Incidentaa(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['description', 'user', 'type']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }
