from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class pokemonForm(FlaskForm):
    pokemon = StringField("Poke'mon Name")
    submit = SubmitField()