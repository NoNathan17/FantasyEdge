from django.db import models

# Create your models here.

class News(models.Model):
    header = models.CharField(max_length=500, unique=True)
    description = models.TextField()
    fantasy_impact = models.TextField()
    image = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.header}'
