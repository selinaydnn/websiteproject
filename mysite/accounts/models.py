from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager





class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','last_name', 'email']




    def __str__(self):
        return self.username