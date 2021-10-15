from django.forms import ModelForm
from django import forms
from .models import *

class CarForm(ModelForm):
    class Meta:
        model = CarImage
        fields = '__all__'

