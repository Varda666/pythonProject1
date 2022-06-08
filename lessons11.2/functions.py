import json
from pprint import pp

f = open("candidates.json")
file = json.load(f)

def load_candidates_from_json():
    list_candidates = []
    for dict in file:
        list_candidates.append(dict["name"])
    return list_candidates
pp(load_candidates_from_json())


def get_candidate(id):
    list_candidates = ""
    for dict in file:
        if id == dict["id"]:
            list_candidates += f'{dict["name"]}\n'
    return '<pre>' + list_candidates + '</pre>'

def get_candidates_by_name(name):
    list_candidates = ""
    for dict in file:
        if name == dict["name"]:
            list_candidates += f'{dict["name"]}\n'
    return '<pre>' + list_candidates + '</pre>'

def get_candidates_by_skill(skill):
    list_candidates = ""
    for dict in file:
        list_skills = dict["skills"].lower().strip().split(', ')
        if skill in list_skills:
            list_candidates += f'{dict["name"]}\n'
    return '<pre>' + list_candidates + '</pre>'