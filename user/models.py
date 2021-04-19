from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    Custom model for user. Django recommends to use a custom model as the model used for authentication can't be altered
    later.
    """
    pass
