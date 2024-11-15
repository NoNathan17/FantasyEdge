# Generated by Django 5.1.1 on 2024-11-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('team', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=20)),
                ('info', models.URLField(default='N/A')),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=4)),
            ],
        ),
    ]
