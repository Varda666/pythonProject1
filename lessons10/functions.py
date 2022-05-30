import json
f = open("candidates.json")
file = json.load(f)

def get_list_candidates():
    """Получает список кандидатов"""
    list_candidates = ''
    for dict in file:
        list_candidates += f'{dict["name"]}\n'
        list_candidates += f'{dict["position"]}\n'
        list_candidates += f'{dict["skills"]}\n'

    return '<pre>' + list_candidates + '</pre>'

def get_some_candidate_by_id(pk):
    """Получает кандидата по номеру id"""
    list_candidates = ''
    for dict in file:
        if pk == dict["id"]:
            list_candidates += f'<img src=\"{dict["picture"]}\">\n'
            list_candidates += f'{dict["name"]}\n'
            list_candidates += f'{dict["position"]}\n'
            list_candidates += f'{dict["skills"]}\n'
            list_candidates += f'\n'

    return '<pre>' + list_candidates + '</pre>'

def get_list_candidates_with_skill(skill):
    """Получает список кандидатов с определенным скиллом"""
    list_candidates = ''
    for dict in file:
        list_skills = dict["skills"].lower().strip().split(', ')
        if skill in list_skills:
            list_candidates += f'{dict["name"]}\n'
            list_candidates += f'{dict["position"]}\n'
            list_candidates += f'{dict["skills"]}\n'

    return list_candidates