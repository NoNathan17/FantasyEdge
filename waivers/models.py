from django.db import models

# Create your models here.

class Waiver(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    info = models.URLField(max_length=200, default='N/A')
    own_percentage = models.CharField(max_length=20)

