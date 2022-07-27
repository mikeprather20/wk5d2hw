from flask import Blueprint, render_template, request
from .forms import pokemonForm


from app.models import Pokemon

poke = Blueprint('poke', __name__, template_folder='poke_template')
import requests
@poke.route('/pokemon', methods=["GET", "POST"])
def pokedex(pokemon):

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
            "hp": data['stats'][0]['base_stat'],
            'attack': data['stats'][1]['base_stat'],
            'defense': data['stats'][2]['base_stat']
        }
        return my_dict
    else:
        return "Error"

    return render_template('pokemon.hml', form = form)