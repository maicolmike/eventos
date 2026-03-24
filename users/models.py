from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    identificacion = models.CharField(max_length=100, unique=True)
    nombres = models.CharField(max_length=255)
    agencia = models.CharField(max_length=255)