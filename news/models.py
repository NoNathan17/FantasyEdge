from django.db import models

# Create your models here.

class News(models.Model):
    header = models.CharField(max_length=30)
    description = models.TextField()
    fantasy_impact = models.TextField()
