from django.db import models

# Create your models here.

import uuid

class Car(models.Model):
    car_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    registration=models.CharField(max_length=7,unique=True)
    make=models.CharField(max_length=40)
    model=models.CharField(max_length=40)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    registration_date=models.DateField()