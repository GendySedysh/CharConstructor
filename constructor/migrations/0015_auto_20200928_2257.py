# Generated by Django 3.0.8 on 2020-09-28 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0014_auto_20200928_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.ProfessionList'),
        ),
    ]
