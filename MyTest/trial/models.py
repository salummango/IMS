from django.db import models
from django.utils import timezone
# Create your models here.
class computer(models.Model):
    computer_name=models.CharField(max_length=30)
    computer_type=models.CharField(max_length=30)
    computer_OS=models.CharField(max_length=30)
    computer_RAM=models.CharField(max_length=30)
    computer_HDD=models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    def _str_(self):
        return self.name
    
#creating module for cars
class Cars(models.Model):
    car_name=models.CharField(max_length=255)
    manufacture=models.CharField(max_length=255)
    engine_type=models.CharField(max_length=255)
    color=models.CharField(max_length=255)
    automation=models.CharField(max_length=255)
    speed=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    date_created=models.DateTimeField(default=timezone.now)
    date_updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.car_name
    

