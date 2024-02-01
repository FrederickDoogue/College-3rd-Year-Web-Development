# Student Name: Rachel Doogue
# Student Number: C00237335
# Description: Bulding a Flask based webapp with Jinja2

from flask import Flask, request, render_template

import datetime

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "index.html", title="Home Page", heading="Welcome to my Webapp!",
    )


@app.get("/personal")
def display_personal():
    return render_template("personal.html", title="Personal Page", heading="About Me",)


@app.get("/cv")
def display_cv():
    return render_template("cv.html", title="CV Page", heading="My CV",)


@app.get("/technologies")
def display_tech():
    return render_template(
        "tech.html",
        title="Computing Technologies Page",
        heading="Choose a Computing Technology to Read About",
    )


@app.get("/java")
def display_java():
    return render_template(
        "java.html", title="Java Page", heading="Read About my Experience with Java",
    )


@app.get("/html")
def display_html():
    return render_template(
        "html.html", title="HTML Page", heading="Read About my Experience with HTML",
    )


@app.get("/os")
def display_os():
    return render_template(
        "os.html",
        title="OS Page",
        heading="Read About my Experience with Operating Systems",
    )


@app.get("/interests")
def display_interests():
    return render_template(
        "interests.html", title="Interests Page", heading="My Interests",
    )


@app.get("/showform")
def display_form():
    return render_template(
        "form.html", title="Welcom Form", heading="Please fill in the form",
    )


@app.post("/processform")
def save_data():
    the_first = request.form["first"]
    the_last = request.form["last"]
    the_email = request.form["email"]
    the_message = request.form["message"]
    with open("comments.txt", "a") as sf:
        print(f"{the_first}, {the_last}, {the_email}, {the_message}", file=sf)
    return f"Thanks, {the_first} at {the_email} for your short message: {the_message}"


if __name__ == "__main__":
    app.run(debug=True)
