# Generated by Django 5.1.1 on 2024-09-30 17:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
