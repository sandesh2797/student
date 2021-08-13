from typing import MutableMapping
from django.db import models
from django.dispatch import receiver

class myfit(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.TextField(null=True)
    object=models.Manager()


 




# Create your models here.
