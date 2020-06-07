import os

from flask import Flask, session, render_template, request, url_for, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from flask_googlemaps import GoogleMaps

app = Flask(__name__)
my_api_key= os.getenv("api_key", None)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)



@app.route("/")
def index():
    return render_template("index.html", my_api_key=my_api_key)

@app.route("/notice", methods =["GET", "POST"])
def notice():
    address = request.form.get("address")
    if not address:
        return redirect("/")
    location = Address(address=address)
    db.session.add(location)
    db.session.commit()
    addresses = Address.query.all()
    return render_template("notice.html", addresses=addresses)

@app.route("/action1", methods =["GET", "POST"])
def action1():
    notice = request.form.get('notice1')
    try:
        address_id = int(request.form.get("address_id"))
    except ValueError:
        return render_template("failure.html", message="Something went wrong with getting notice and address.")

    address = Address.query.get(address_id)
    if not address:
        return render_template("failure.html", message="Something went wrong with validating the id with address.")

    address.add_notice(notice)
    addresses = Address.query.all()
    return render_template("action1.html", title="30/60 Day Notice", addresses=addresses, my_api_key=my_api_key)

@app.route("/action2", methods =["GET", "POST"])
def action2():
    notice = request.form.get('notice2')
    try:
        address_id = int(request.form.get("address_id"))
    except ValueError:
        return render_template("failure.html", message="Something went wrong with getting notice and address.")

    address = Address.query.get(address_id)
    if not address:
        return render_template("failure.html", message="Something went wrong with getting the address.")

    address.add_notice(notice)
    return render_template('action2.html', title="3 day notice")

@app.route("/action3", methods =["GET", "POST"])
def action3():
    notice = request.form.get('notice3')

    try:
        address_id = int(request.form.get("address_id"))
    except ValueError:
        return render_template("failure.html", message="Something went wrong with getting notice and address.")

    address = Address.query.get(address_id)
    if not address:
        return render_template("failure.html", message="Something went wrong with getting the address.")


    address.add_notice(notice)
    return render_template('action3.html', title="unlawful detainer notice")