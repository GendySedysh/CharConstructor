from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
race_fs = FileSystemStorage(location='/static/img/races')
based_stats = ['Интеллект', 'Воля', 'Ловкость', 'Телосложение', 'Ремесло', 'Эмпатия', 'Эмпатия', 'Реакция']


class RaceList(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    img = models.ImageField(upload_to='static/img/races')
    for_js = models.CharField(max_length=30)
    name_eng = models.CharField(max_length=30, default='race name')
    info = models.CharField(default=f'Тут информация о {name}, описание фишек и тп', max_length=600)

    def __str__(self):
        return self.name


class StatList(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    short_name = models.CharField(max_length=10, default=f'NAME')
    name_eng = models.CharField(max_length=30, default='stat name')
    skill_base = models.BooleanField(default=False)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SkillList(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    name_eng = models.CharField(max_length=30, default='stat name')
    info = models.CharField(default=f'Тут информация о НАЗВАНИЕ НАВЫКА, описание фишек и тп', max_length=300)
    depended_stat = models.ForeignKey(StatList(skill_base=True), on_delete=models.CASCADE, blank=True, null=True)
    unique = models.BooleanField(default=False)
    cost = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(2)])

    def __str__(self):
        return self.name


class ProfessionList(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    img = models.ImageField(upload_to='static/img/professions')
    for_js = models.CharField(max_length=30)
    name_eng = models.CharField(max_length=30, default='profession name')
    info = models.CharField(default=f'Тут информация о НАЗВАНИЕ ПРОФЕССИИ, описание фишек и тп', max_length=300)
    available_race = models.ManyToManyField(RaceList)
    available_skill = models.ManyToManyField(SkillList, blank=True, related_name='skill')

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    race = models.ForeignKey(RaceList, on_delete=models.CASCADE, null=True)
    profession = models.ForeignKey(ProfessionList, on_delete=models.CASCADE, null=True, default='Маг')

    def __str__(self):
        title = f'{self.race} {self.name}'
        return title

    @classmethod
    def create(cls, character, race):
        new_char_race = cls(character, race)
        new_char_race.save()


class CharacterStat(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
    skill_base = models.BooleanField(default=False)
    main = models.BooleanField(default=False)

    def __str__(self):
        title = f'{self.character} {self.name}'
        return title

    @classmethod
    def create(cls, name, value, character, main):
        if name in based_stats:
            stat = cls(name=name, value=value, character=character, main=main, skill_base=True)
            stat.save()
        else:
            stat = cls(name=name, value=value, character=character, main=main)
            stat.save()


class CharacterSkill(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    value = models.IntegerField(default=0, null=True)
    info = models.CharField(default=f'Тут информация о НАЗВАНИЕ НАВЫКА, описание фишек и тп', max_length=300)
    cost = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(2)])
    unique = models.BooleanField(default=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
    depended_stat = models.ForeignKey(CharacterStat(skill_base=True), on_delete=models.CASCADE, blank=True, null=True)

    @classmethod
    def create(cls, name, value, info, cost, unique, character, depended_stat):
        skill = cls(name=name, value=value, info=info, cost=cost, unique=unique,
                    character=character, depended_stat=depended_stat)
        skill.save()
