from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    
