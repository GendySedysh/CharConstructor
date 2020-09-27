from django.contrib import admin

# Register your models here.
from constructor.models import RaceList, ProfessionList, StatList, SkillList, Character\
, CharacterStat, CharacterSkill, CharacterRace


admin.site.register(RaceList)
admin.site.register(ProfessionList)
admin.site.register(StatList)
admin.site.register(SkillList)
admin.site.register(Character)
admin.site.register(CharacterStat)
admin.site.register(CharacterSkill)
admin.site.register(CharacterRace)
