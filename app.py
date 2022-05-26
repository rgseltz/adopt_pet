from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'loverboy24'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_pet'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

