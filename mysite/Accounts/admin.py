
from django.contrib import admin
from .models import Login  # Import the Login model

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('signin',)  # Display the SignIn field in the admin list view
    # Add other configurations as needed
