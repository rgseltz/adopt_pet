from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional

class NewPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = SelectField("Pet Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('pkp', 'Porcupine')])
    photo_url = StringField("Input link of pet picture")
    age = IntegerField("Age (in years)")
    notes = TextAreaField("Tell us more about your pet")
    
class UpdatePetForm(FlaskForm):   
    photo_url = StringField("Input link of pet picture")
    notes = TextAreaField("Tell us more about your pet")
    available = BooleanField("Available for adoption")

