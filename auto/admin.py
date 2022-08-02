from django.contrib import admin
from .models import *

@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "who", "phone", "password")

@admin.register(CreateAuto)
class CreateAutoAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "image", "year", "mileage", "price")





