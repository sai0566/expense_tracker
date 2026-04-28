from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    valid=RegexValidator(r'[6-9][0-9]{9}',message='valid number starts between 6-9')
    phone=models.CharField(max_length=10,blank=True,validators=[valid],null=True)
    address=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username
