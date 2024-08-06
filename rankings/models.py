from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')
    
class Quarterback(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')

class RunningBack(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')

class WideReciever(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')

class TightEnd(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')

class Kicker(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')

class Defense(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    bye_week = models.CharField(max_length=20)
    adp = models.CharField(max_length=20, default='N/A')


    