from django.contrib import admin
from .models import SignIn

@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')

# Register your models here.
