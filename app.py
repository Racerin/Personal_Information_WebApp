import os, sys, time, smtplib
from flask import Flask, request, render_template, send_from_directory, url_for, redirect, jsonify, session
import PARAM
from markupsafe import Markup
from Library import Database, Person, CustomFlask
import Library


app = Flask(__name__)


# database = Database.JsonDatabase()
database = Database.SQLiteDatabase(filename=PARAM.DATABASE.FILENAME)


app.secret_key = b"fslku89utwknt5w49iwjifsi9384uq9439-3"
# app.session_interface = CustomFlask.MySessionInterface()
app.session_interface.session_class = CustomFlask.MySession


app.config["DEBUG"] = True
# app.config["ENV"] = "production" #default value
app.config["TESTING"] = True


#Jinja Config
def print2(obj): print(obj); return obj
app.jinja_env.filters['print'] = print2



@app.route("/")
def index():
    """Home page"""
    return render_template(PARAM.HTML.HOME)


@app.route("/")
def home():
    """Home page"""
    return render_template(PARAM.HTML.HOME)


@app.route("/login", methods=["POST", "GET"])
def login():
    """Login to an existing account"""
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    else:
        return render_template(PARAM.HTML.LOGIN)
        

@app.route("/logout", methods=["POST"])
def logout():
    """Logout an existing account"""
    return "Shit"


@app.route("/create_account", methods=["GET", "POST"])
def signup():
    """Create a new user account"""
    if request.method == "POST":
        session["username"] = request.form["username"]
                                                        #Update username and password to database
        return redirect(url_for("index"))
    else:
        return render_template(PARAM.HTML.SIGNUP)


@app.route("/form", methods=["POST", "GET"])
def form():
    """Form for registering a personality."""
    if request.method == "GET":
        return render_template(PARAM.HTML.FORM, genders=PARAM.GENDER.FORM)
    elif request.method == "POST":
        print("This is FORM:", request.form)
        person = Library.Person.from_dict(request.form)
        if person.valid():
            print("GT Boss: ", person)
            database.register_person(person)
            # return render_template(PARAM.HTML.SUBMIT_SUCCESS, persons=database.get_persons())
            # return redirect("/success")
            return redirect(url_for("success"))
        else:
            return render_template(PARAM.HTML.SUBMIT_FAILURE)


@app.route("/success")
def success():
    return render_template(PARAM.HTML.SUBMIT_SUCCESS, persons=database.get_persons())


@app.route("/failure")
def failure():
    return render_template(PARAM.HTML.SUBMIT_FAILURE)


@app.route("/about")
def about():
    return render_template(PARAM.HTML.ABOUT)


@app.route("/contact")
def contact():
    return render_template(PARAM.HTML.CONTACT)


#not working
# @app.route("/<path:filename>")
def others(filename):
    str1 = f"{filename}.html"
    render_template(str1)


@app.errorhandler(404)
def page_not_found(error):
    render_template(PARAM.HTML.ERROR404)


@app.errorhandler(500)
def server_mess_up(eror):
    return "My bad. The server have some issues to deal with."


#https://stackoverflow.com/a/48107969/6556801
@app.route('/img/<path:filename>')
def send_file(filename):
    # return send_from_directory(app.static_folder, filename)
    str1 = r'/'.join(['images',filename])
    return send_from_directory(app.static_folder, str1)


@app.route("/json")
def json_person():
    return Person().to_json()


@app.route("/list")
def list_something():
    """Only return a dictionary, string or *tuple(Check out Flask Responses). """
    return "Crap-o smoke yuh pipe.".split(" ")


if __name__ == "__main__":
    app.run()
