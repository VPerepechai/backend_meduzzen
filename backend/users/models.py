from core.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, TimeStampedModel):
    image_path = models.CharField()
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
