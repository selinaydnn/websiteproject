from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self,username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class SignIn(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Specify the manager for the model
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def _str_(self):
        return self.username


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    # Add your custom fields here
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Specify the manager for the model
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def _str_(self):
        return self.username