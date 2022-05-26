import json
f = open("candidates.json")
file = json.load(f)

list_candidates = ''
for dict in file:
    list_skills = dict["skills"].lower().strip().split(', ')






