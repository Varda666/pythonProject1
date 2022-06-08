import functions
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def page_all_candidates():
	candidates = functions.load_candidates_from_json()
	return render_template("list.html", candidates=candidates)



if __name__ == "__main__":
	app.run()