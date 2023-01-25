from django.core import validators
from django import forms
from .models import User
class Ticket(forms.ModelForm):
  class Meta:
    model = User
    fields = '__all__'
    labels = {'sNumber':"SeatNumber",'name':"Name",'email':"Email",'password':"Password",'image':"Image",'price':"TPrice"}


