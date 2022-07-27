from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class pokemonForm(FlaskForm):
    pokemon = StringField('pokemon', validators=[DataRequired])
    submit = SubmitField()