from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TherapistSignup

class TherapistAdmin(UserAdmin):
    # Customize the display and fields if needed
    list_display = ('username', 'email', 'name', 'last_name', 'education', 'age', 'gender')
    search_fields = ('username', 'email', 'name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'last_name', 'email', 'education', 'age', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Register the Therapist model with the customized admin
admin.site.register(TherapistSignup, TherapistAdmin)
