from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional

class NewPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Pet Species")
    photo_url = StringField("Input link of pet picture")
    age = IntegerField("Age (in years)")
    notes = TextAreaField("Tell us more about your pet")

