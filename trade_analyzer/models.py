from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    info = models.URLField(max_length=200, default='N/A')
    rating = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
