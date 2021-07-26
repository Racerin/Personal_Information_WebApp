import os, sys, time, smtplib
from flask import Flask, request, render_template, url_for, redirect
import PARAM
from markupsafe import Markup
from Library import Database
import Library


database = Database.JsonDatabase()
persons = database.recall(PARAM.JSON.PERSONS, default=[])


app = Flask(__name__)


# app.route("/personal_form")
@app.route("/")
def form():
    return render_template(PARAM.HTML.FORM)


@app.route("/register", methods=["POST"])
def register():
    person = Library.Person.from_dict(request.form)
    if person.valid():
        persons.append(person)
        return render_template(PARAM.HTML.SUBMIT_SUCCESS, persons=persons)
        # return redirect("/success")
        # return redirect(url_for("success"))
    else:
        return render_template(PARAM.HTML.SUBMIT_FAILURE)


@app.route("/success")
def success():
    # return "GWAM"
    return render_template(PARAM.HTML.SUBMIT_SUCCESS, persons=persons)


@app.route("/failure")
def failure():
    return render_template(PARAM.HTML.SUBMIT_FAILURE)


if __name__ == "__main__":
    app.run()
    database.submit(PARAM.JSON.PERSONS, persons)
