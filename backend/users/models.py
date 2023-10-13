from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    image_path = models.CharField()
