from django.db import models


class TimeStampedModel(models.Model):
    """Basic Model for timestamps"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #This meta option indicates that TimeStampedModel is an abstract model
