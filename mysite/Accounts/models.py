from django.db import models
from signin.models import CustomUser  # Import the SignIn model

class Login(models.Model):
    signin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)