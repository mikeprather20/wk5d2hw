from flask import Blueprint, request
from .forms import pokemonForm


from app.models import Pokemon

poke = Blueprint('poke', __name__, template_folder='poke_template')

@poke.route('/pokemon', methods=["GET", "POST"])
def pokedex(pokemon):
    form = pokemonForm()
    if request.method == "POST":
        pokemon =='pokemon'
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        data = response.json()
        pokemon_info = []
        pokedex = {
        'Name' : data['forms'][0]['name'].title(),
        'Ability' : data['abilities'][0]['ability']['name'].title(),
        'Image' : data['sprites']['front_shiny'],
        'ATK Stat' : data['stats'][0]['base_stat'],
        'HP Stat' : data['stats'][1]['base_stat'],
        'DEF Stat' : data['stats'][2]['base_stat']
        }
        requests.get(f'pokeapi.co/v1/pokemon/{pokemon}')
        pokemon_info.append(pokedex)
        return pokemon_info
    else:
        return