from flask import Flask, render_template, request, session
from flask_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("test4.html")

@app.route("/about")
def about():
    return render_template("test4_1.html")

@app.route("/projects")
def projects():
    return render_template("test4_2.html")

@app.route("/contact")
def contact():
    return render_template("test4_3.html")

@app.route("/addnote", methods=["GET", "POST"])
def addnote():
        if session.get("note") is None:
            session["note"] = []
        if request.method == "POST":
            note = request.form.get("name")
            session["note"].append(note)
        return render_template("test4.html", notes= session["note"])
