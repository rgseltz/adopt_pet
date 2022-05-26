from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import NewPetForm
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

@app.route('/pets/new', methods = ["GET", "POST"])
def add_pet_form():
    form = NewPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new-pet-form.html', form=form)
    