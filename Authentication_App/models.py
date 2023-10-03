from django.db import models
from django.contrib.auth.models import AbstractUser
from .usermanager import user_manager

# Create your models here.


class user(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    Type = models.CharField(max_length=50, choices=(
        ('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs')))
    first_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    Date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, choices=(
        ('Indian', 'Indian'), ('Foreigners', 'Foreigners')))
    Where_do_you_live = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = user_manager()
