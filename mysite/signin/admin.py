from django.contrib import admin
from .models import SignIn  # Import your SignIn model

# Register the SignIn model with the admin site
@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')  # Display these fields in the admin list view
    # Add other configurations as needed
