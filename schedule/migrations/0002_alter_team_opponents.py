# Generated by Django 5.0.7 on 2024-08-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='opponents',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
