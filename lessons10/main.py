import functions
from flask import Flask
app = Flask(__name__)

@app.route("/")
def page_all_candidates():
    return functions.get_list_candidates()

@app.route("/candidate/<int:pk>")
def page_some_candidate(pk):
    return functions.get_some_candidate_by_id(pk)

@app.route("/skills/<skill>")
def page_candidate_with_skill(skill):
    return functions.get_list_candidates_with_skill(skill)

if __name__ == "__main__":
	app.run()