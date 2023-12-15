from django.db import models
from signin.models import SignIn  # Import the SignIn model

class Login(models.Model):
    signin = models.OneToOneField(SignIn, on_delete=models.CASCADE)