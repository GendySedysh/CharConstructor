# Generated by Django 3.0.8 on 2020-08-11 17:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0006_auto_20200806_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterSkill',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('value', models.IntegerField(default=0, null=True)),
                ('info', models.CharField(default='Тут информация о НАЗВАНИЕ НАВЫКА, описание фишек и тп', max_length=300)),
                ('cost', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('unique', models.BooleanField(default=False)),
                ('character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.Character')),
                ('depended_stat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.CharacterStat')),
            ],
        ),
    ]