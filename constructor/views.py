from django.shortcuts import render, redirect
from django.views.generic import ListView
from constructor.models import RaceList, ProfessionList, StatList, SkillList, Character, \
    CharacterStat, CharacterSkill, CharacterRace
# Create your views here.

character_data = {}


# рассчитывает очки навыков персонажа
def skill_point_count(char_name):
    character = Character.objects.get(name=char_name)
    intelligence = CharacterStat.objects.get(character=character, name='Интеллект')
    reaction = CharacterStat.objects.get(character=character, name='Реакция')
    summ = intelligence.value + reaction.value
    print(f'У {char_name}, обычных очков навыков {summ}')
    return summ


# возвращает словарь {'имя характеристики': 'значение характеристики'} персонажа
def stat_list_creation(char_name):
    stat_value_list = {}
    character = Character.objects.get(name=char_name)
    stats = StatList.objects.filter(skill_base=True)
    character_stats = CharacterStat.objects.filter(character=character, skill_base=True)
    for stat in stats:
        for char_stat in character_stats:
            if stat.name == char_stat.name:
                stat_value_list[stat] = char_stat
    return stat_value_list


# возвращает профессиональные навыки
def prof_skills(prof_name):
    profession = ProfessionList.objects.get(name=prof_name)
    prof_skill_list = profession.available_skill.all()
    return prof_skill_list


# возвращает остальные навыки
def other_skills(prof_name):
    non_prof_skill_list = []
    profession = ProfessionList.objects.get(name=prof_name)
    prof_skill_list = profession.available_skill.all()
    skill_list = SkillList.objects.filter(unique=False)
    for skill in skill_list:
        if skill in prof_skill_list:
            pass
        else:
            non_prof_skill_list.append(skill)
    return non_prof_skill_list


def race_list(request):
    error_exist = False
    race_model = RaceList.objects.filter()
    char_model = Character.objects.filter()
    context = {'races': race_model, 'char_model': char_model}
    if request.method == 'POST':
        character_race = request.POST.get('race_pick', False)
        newchar_name = request.POST.get('char_name')

        if character_race == 'Ведьмак':
            return render(request, 'witcher_create.html', context)

        for char in Character.objects.filter():
            if char.name == newchar_name:
                error_text = 'Персонаж с таким именем уже есть, введите другое'
                print(error_text)
                context['error'] = error_text
                error_exist = True

        if error_exist:
            return render(request, 'race_list.html', context)
        else:
            Character.create(newchar_name)
            char = Character.objects.get(name=newchar_name)
            CharacterRace.create(character_race, char)
            print(f'Имя персонажа {newchar_name}')
            print(f'Выбранная расса {character_race}')
            character_data['char_name'] = newchar_name
            character_data['char_race'] = character_race
            return redirect('/prof_pick')
    return render(request, 'race_list.html', context)


def prof_list(request):
    race = character_data['char_race']
    picked_race = RaceList.objects.filter(name=race)
    profession_list = ProfessionList.objects.filter(available_race=picked_race[0])
    context = {'professions': profession_list, 'char_data': character_data}
    if request.method == 'POST':
        character_profession = request.POST.get('prof_pick', False)
        print(f'Выбранная профессия {character_profession}')
        character_data['char_prof'] = character_profession
        return redirect('/stats')
    return render(request, 'prof_list.html', context)


def stat_pick(request):
    stat_list = StatList.objects.filter(main=True)
    sec_stat_list = StatList.objects.filter(main=False)
    context = {'main_stat': stat_list, 'sec_stat': sec_stat_list, 'char_data': character_data}
    if request.method == 'POST':
        char_name = character_data['char_name']
        character = Character.objects.get(name=char_name)
        for stat in StatList.objects.filter():
            stat_value = request.POST.get(stat.name_eng, False)
            main_stat = CharacterStat
            main_stat.create(stat.name, stat_value, character, True)
        return redirect('/skills')
    return render(request, 'stat_pick.html', context)


def skill_pick(request):
    char_name = character_data['char_name']
    picked_prof = character_data['char_prof']
    profession = ProfessionList.objects.get(name=picked_prof)
    context = {'profession': profession, 'char_data': character_data,
               'prof_skills': prof_skills(picked_prof), 'other_skills': other_skills(picked_prof),
               'skill_points': skill_point_count(char_name), 'stat_list': stat_list_creation(char_name)}
    if request.method == 'POST':
        character = Character.objects.get(name=char_name)
        for prof_skill in prof_skills(picked_prof):
            for stat in CharacterStat.objects.filter(character=character):
                if stat.name == prof_skill.depended_stat.name:
                    prof_skill_value = request.POST.get(prof_skill.name_eng, False)
                    p_skill = CharacterSkill
                    p_skill.create(prof_skill.name, prof_skill_value, prof_skill.info, prof_skill.cost,
                                   prof_skill.unique, character, stat)
        return redirect('/character')
    return render(request, 'skill_pick.html', context)


def character_sheet(request):
    char_name = character_data['char_name']
    character = Character.objects.filter(name=char_name)
    character_stat_list = CharacterStat.objects.filter(character=character[0])
    character_race = CharacterRace.objects.filter(character=character[0])
    character_skill_list = CharacterSkill.objects.filter(character=character[0])
    context = {'character': character, 'stats': character_stat_list, 'skills': character_skill_list,
               'races': character_race}
    return render(request, 'character_sheet.html', context)

