from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=30)
    opponents = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f'{self.name}'