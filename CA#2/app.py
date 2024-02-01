# Student Name: Rachel Doogue
# Student Number: C00237335
# Description: Extend CA~1 with database support and test suite. Then deploy webapp tp PythonAnywhere.

from flask import Flask, request, render_template
from data_utils import save_data, display_data

import datetime


app = Flask(__name__)

SAVE_FILE = "data/savefile.txt"


@app.route("/")
def index():
    return render_template(
        "index.html", title="Home Page", heading="Welcome to my Webapp!",
    )


@app.route("/personal")
def display_personal():
    return render_template("personal.html", title="Personal Page", heading="About Me",)


@app.route("/cv")
def display_cv():
    return render_template("cv.html", title="CV Page", heading="My CV",)


@app.route("/technologies")
def display_tech():
    return render_template(
        "tech.html",
        title="Computing Technologies Page",
        heading="Choose a Computing Technology to Read About",
    )


@app.route("/java")
def display_java():
    return render_template(
        "java.html", title="Java Page", heading="Read About my Experience with Java",
    )


@app.route("/html")
def display_html():
    return render_template(
        "html.html", title="HTML Page", heading="Read About my Experience with HTML",
    )


@app.route("/os")
def display_os():
    return render_template(
        "os.html",
        title="OS Page",
        heading="Read About my Experience with Operating Systems",
    )


@app.route("/interests")
def display_interests():
    return render_template(
        "interests.html", title="Interests Page", heading="My Interests",
    )


@app.route("/showform")
def display_form():
    return render_template(
        "form.html", title="Welcom Form", heading="Please fill in the form",
    )


@app.route("/processform")
def save_data():
    the_first = request.form["first"]
    the_last = request.form["last"]
    the_email = request.form["email"]
    the_message = request.form["message"]
    save_data(the_first, the_last, the_email, the_message)
    return render_template(
        "message.html",
        title="Your message ",
        heading="Message Board",
        the_first=request.form["first"],
        the_last=request.form["last"],
        the_email=request.form["email"],
        the_message=request.form["message"],
    )


@app.route("/messageboard")
def display_messageboard():
    results = display_data()
    return str(results)


if __name__ == "__main__":
    app.run(debug=True)
