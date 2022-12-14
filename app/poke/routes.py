from flask import Blueprint, render_template, request
from .forms import pokemonForm
import requests

#from app.models import Pokemon

poke = Blueprint('poke', __name__, template_folder='poke_template')



@poke.route('/pokemon', methods = ['GET', 'POST'])
def pokedex():
    form = pokemonForm()
    my_dict = {}

    if request.method == "POST":
        poke_name = form.name.data

        url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        res = requests.get(url)
        if res.ok:
            data = res.json()
            my_dict = {
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'img_url': data['sprites']['front_shiny'],
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }
        else:
            return "ERROR"

    return render_template('pokemon.html', form = form, pokemon = my_dict)