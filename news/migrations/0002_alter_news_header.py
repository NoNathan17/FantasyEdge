# Generated by Django 5.0.7 on 2024-09-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='header',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]