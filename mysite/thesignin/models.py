from django.db import models
from django.contrib.auth.models import AbstractUser
class TherapistSignup(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    email = models.EmailField(unique=True)


    def __str__(self):
        return f"{self.name} {self.last_name}"
