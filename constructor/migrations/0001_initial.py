# Generated by Django 3.0.8 on 2020-08-02 20:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MainStatList',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('name_eng', models.CharField(default='stat name', max_length=30)),
                ('skill_base', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RaceList',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='static/img/races')),
                ('for_js', models.CharField(max_length=30)),
                ('bonus1', models.CharField(max_length=60)),
                ('bonus1_num', models.IntegerField(default=0)),
                ('bonus2', models.CharField(max_length=60)),
                ('bonus2_num', models.IntegerField(default=0)),
                ('bonus3', models.CharField(max_length=60)),
                ('bonus3_num', models.IntegerField(default=0)),
                ('other_bonus', models.CharField(max_length=60)),
                ('name_eng', models.CharField(default='race name', max_length=30)),
                ('info', models.CharField(default='Тут информация о <django.db.models.fields.CharField>, описание фишек и тп', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SecStatList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('name_eng', models.CharField(default='stat name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SkillList',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('name_eng', models.CharField(default='stat name', max_length=30)),
                ('info', models.CharField(default='Тут информация о НАЗВАНИЕ НАВЫКА, описание фишек и тп', max_length=300)),
                ('unique', models.BooleanField(default=False)),
                ('depended_stat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.MainStatList')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionList',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='static/img/professions')),
                ('for_js', models.CharField(max_length=30)),
                ('name_eng', models.CharField(default='profession name', max_length=30)),
                ('info', models.CharField(default='Тут информация о НАЗВАНИЕ ПРОФЕССИИ, описание фишек и тп', max_length=300)),
                ('available_race', models.ManyToManyField(to='constructor.RaceList')),
                ('available_skill', models.ManyToManyField(blank=True, related_name='skill', to='constructor.SkillList')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('main', models.BooleanField(default=False)),
                ('character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bonus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.MainStatList')),
                ('character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.Character')),
            ],
        ),
    ]
