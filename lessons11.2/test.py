import json
f = open("candidates.json")
file = json.load(f)
name_ = input()
list_candidates = []
for dict in file:
    name = dict["name"].lower().strip().split()
    if name_ in name:
        print(dict["name"])
    else:
        pass