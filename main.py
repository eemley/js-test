from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/workout/")
def workout():
    return render_template("fitness.html")

@app.route("/workout/results_lo")
def lo():
    return render_template("results_lo.html")

@app.route("/workout/results_hi")
def hi():
    return render_template("results_hi.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")

if __name__ == "__main__":
    app.run(debug=True)