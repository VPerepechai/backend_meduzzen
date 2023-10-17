from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    image_path = models.CharField()
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
