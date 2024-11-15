from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    info = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        return f'{self.name}'
    
class Quarterback(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    info = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        return f'{self.name}'

class RunningBack(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    info = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        return f'{self.name}'

class WideReciever(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    info = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        return f'{self.name}'

class TightEnd(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    info = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        return f'{self.name}'

class Kicker(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    info = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        return f'{self.name}'

class Defense(models.Model):
    name = models.CharField(max_length=100, unique=True)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    info = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        return f'{self.name}'


    