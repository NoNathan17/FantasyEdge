# Generated by Django 5.1.1 on 2024-09-30 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
    ]