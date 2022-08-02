from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["username", "first_name", "last_name", "who", "phone", "password"]

class CreateAutoModelForm(forms.ModelForm):
    class Meta:
        model = CreateAuto
        fields = ["brand", "model", "image", "year", "mileage", "price"]


