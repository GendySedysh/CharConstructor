# Generated by Django 3.0.8 on 2020-08-04 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0002_auto_20200802_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilllist',
            name='cost',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
