import json
from pprint import pp

f = open("candidates.json")
file = json.load(f)

def load_candidates_from_json():
    """Возвращает список кандидатов"""
    list_candidates = []
    for dict in file:
        list_candidates.append(dict["name"])
    return list_candidates


def get_candidate(id):
    """Возвращает кандидата по номеру id"""
    list_candidates = {}
    for dict in file:
        if id == dict["id"]:
            list_candidates['id'] = dict["id"]
            list_candidates['name'] = dict["name"]
            list_candidates['position'] = dict["position"]
            list_candidates['picture'] = dict["picture"]
            list_candidates['skills'] = dict["skills"]
    return list_candidates


def get_candidates_by_name(name):
    """Возвращает кандидата по имени"""
    for dict in file:
        name_ = dict["name"].lower().strip().split()
        if name in name_:
            return dict["name"]
        else:
            pass

def get_number_candidates_by_name(name):
    """Возвращает количество кандидатов с именем"""
    number_of_candidates = 0
    for dict in file:
        name_ = dict["name"].lower().strip().split()
        if name in name_:
            number_of_candidates += 1
        else:
            pass
    return number_of_candidates


def get_candidates_by_skill(skill):
    """Возвращает кандидата по навыку"""
    list_candidates = ""
    for dict in file:
        list_skills = dict["skills"].lower().strip().split(', ')
        if skill in list_skills:
            list_candidates += f'{dict["name"]}\n'
    return '<pre>' + list_candidates + '</pre>'

def get_number_of_candidates_with_skill(skill):
    """Возвращает количество кандидатов с навыком"""
    number_of_candidates_with_skill = 0
    for dict in file:
        list_skills = dict["skills"].lower().strip().split(', ')
        if skill in list_skills:
            number_of_candidates_with_skill += 1
        else:
            pass
    return number_of_candidates_with_skill