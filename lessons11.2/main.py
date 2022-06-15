import functions
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def page_all_candidates():
	candidates = functions.load_candidates_from_json()
	return render_template("list.html", candidates=candidates)

@app.route("/candidate/<int:id>")
def get_candidate(id):
	candidate = functions.get_candidate(id)
	return render_template("single.html", candidate=candidate)

@app.route("/search/<name>")
def get_candidate_by_name(name):
	names = functions.get_candidates_by_name(name.lower())
	return render_template("search.html", name=names, number=len(names))

@app.route("/skill/<skill_name>")
def get_candidates_by_skill(skill_name):
	candidates_with_skill = functions.get_candidates_by_skill(skill_name.lower())
	return render_template("skill.html", candidates_with_skill=candidates_with_skill, number_of_candidates_with_skill= len(candidates_with_skill), skill_name=skill_name)



if __name__ == "__main__":
	app.run()