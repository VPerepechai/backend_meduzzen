from core.models import TimeStampedModel
from django.db import models
from users.models import User


# Create your models here.
class Company(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
