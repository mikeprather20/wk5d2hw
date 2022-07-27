from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class pokemonForm(FlaskForm):
    name = StringField("Pokemon Name")
    submit = SubmitField()