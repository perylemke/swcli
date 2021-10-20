import fire
import json
from httpx import get
from models import Film, Person, Planet, Specie, Starship, Vehicle

# Settings
BASE_URL='https://swapi.dev/api/'


def films(title):
    "Returns a SW film"
    response = get(BASE_URL+'films/?search='+title).json()

    for response_dict in response['results']:
        species_list = []
        for specie in response_dict['species']:
            specie_itens = get(specie).json()['name']
            species_list.append(specie_itens)

        starships_list = []
        for starship in response_dict['starships']:
            starship_itens = get(starship).json()['name']
            starships_list.append(starship_itens)

        vehicles_list = []
        for vehicle in response_dict['vehicles']:
            vehicle_itens = get(vehicle).json()['name']
            vehicles_list.append(vehicle_itens)

        characters_list = []
        for character in response_dict['characters']:
            character_itens = get(character).json()['name']
            characters_list.append(character_itens)

        planets_list = []
        for planet in response_dict['planets']:
            planet_itens = get(planet).json()['name']
            planets_list.append(planet_itens)

        film_response = {
            "title": response_dict['title'],
            "episode": response_dict['episode_id'],
            "director": response_dict['director'],
            "producer": response_dict['producer'],
            "release_date": response_dict['release_date'],
            "species": species_list,
            "starships": starships_list,
            "vehicles": vehicles_list,
            "characters": characters_list,
            "planets": planets_list,
        }

        film = Film(**film_response)
        yield film.json(ensure_ascii=False, encoder='utf-8')


def people(name):
    "Returns a SW people."
    response = get(BASE_URL+'people/?search='+name).json()

    for response_dict in response['results']:
        homeworld = get(response_dict['homeworld']).json()['name']

        vehicles_list = []
        for vehicle in response_dict['vehicles']:
            vehicle_itens = get(vehicle).json()['name']
            vehicles_list.append(vehicle_itens)

        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        starships_list = []
        for starship in response_dict['starships']:
            starship_itens = get(starship).json()['name']
            starships_list.append(starship_itens)

        character_response = {
            "name": response_dict['name'],
            "height": int(response_dict['height'])/100,
            "mass": response_dict['mass'],
            "hair_color": response_dict['hair_color'],
            "skin_color": response_dict['skin_color'],
            "birth_year": response_dict['birth_year'],
            "gender": response_dict['gender'],
            "homeworld": homeworld,
            "films": films_list,
            "vehicles": vehicles_list,
            "starships": starships_list,
        }

        person = Person(**character_response)
        yield person.json(ensure_ascii=False, encoder='utf-8')


def planets(name):
    "Returns a SW planet."
    response = get(BASE_URL+'planets/?search='+name).json()

    for response_dict in response['results']:
        residents_list = []
        for resident in response_dict['residents']:
            resident_itens = get(resident).json()['name']
            residents_list.append(resident_itens)

        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        planet_response = {
            "name": response_dict['name'],
            "diameter": response_dict['diameter'],
            "rotation_period": response_dict['rotation_period'],
            "orbital_period": response_dict['orbital_period'],
            "gravity": response_dict['gravity'],
            "population": response_dict['population'],
            "climate": response_dict['climate'],
            "terrain": response_dict['terrain'],
            "surface_water": response_dict['surface_water'],
            "residents": residents_list,
            "films": films_list,
        }

        planet = Planet(**planet_response)
        yield planet.json(ensure_ascii=False, encoder='utf-8')


def species(name):
    "Return a SW specie."
    response = get(BASE_URL+'species/?search='+name).json()

    for response_dict in response['results']:
        homeworld = get(response_dict['homeworld']).json()['name']

        people_list = []
        for person in response_dict['people']:
            person_itens = get(person).json()['name']
            people_list.append(person_itens)

        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        species_response = {
            "name": response_dict['name'],
            "classification": response_dict['classification'],
            "designation": response_dict['designation'],
            "average_height": int(response_dict['average_height'])/100,
            "average_lifespan": response_dict['average_lifespan'],
            "eye_colors": response_dict['eye_colors'],
            "hair_colors": response_dict['hair_colors'],
            "skin_colors": response_dict['skin_colors'],
            "language": response_dict['language'],
            "homeworld": homeworld,
            "people": people_list,
            "films": films_list,
        }

        specie = Specie(**species_response)
        yield specie.json(ensure_ascii=False, encoder='utf-8')


def starships(name):
    "Return a SW starship."
    response = get(BASE_URL+'starships/?search='+name).json()

    for response_dict in response['results']:
        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        pilots_list = []
        for pilot in response_dict['pilots']:
            pilot_itens = get(pilot).json()['name']
            pilots_list.append(pilot_itens)

        starships_response = {
            "name": response_dict['name'],
            "model": response_dict['model'],
            "starship_class": response_dict['starship_class'],
            "manufacturer": response_dict['manufacturer'],
            "cost": response_dict['cost_in_credits'],
            "length": response_dict['length'],
            "crew": response_dict['crew'],
            "passengers": response_dict['passengers'],
            "max_atmosphering_speed": response_dict['max_atmosphering_speed'],
            "hyperdrive_rating": response_dict['hyperdrive_rating'],
            "mglt": response_dict['MGLT'],
            "cargo_capacity": response_dict['cargo_capacity'],
            "consumables": response_dict['consumables'],
            "films": films_list,
            "pilots": pilots_list,
        }

        starship = Starship(**starships_response)
        yield starship.json(ensure_ascii=False, encoder='utf-8')


def vehicles(name):
    "Return a SW vehicle."
    response = get(BASE_URL+'vehicles/?search='+name).json()

    for response_dict in response['results']:
        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        pilots_list = []
        for pilot in response_dict['pilots']:
            pilot_itens = get(pilot).json()['name']
            pilots_list.append(pilot_itens)

        vehicles_response = {
            "name": response_dict['name'],
            "model": response_dict['model'],
            "vehicle_class": response_dict['vehicle_class'],
            "manufacturer": response_dict['manufacturer'],
            "length": response_dict['length'],
            "cost": response_dict['cost_in_credits'],
            "crew": response_dict['crew'],
            "passengers": response_dict['passengers'],
            "max_atmosphering_speed": response_dict['max_atmosphering_speed'],
            "cargo_capacity": response_dict['cargo_capacity'],
            "consumables": response_dict['consumables'],
            "films": films_list,
            "pilots": pilots_list,
        }

        vehicle = Vehicle(**vehicles_response)
        yield vehicle.json(ensure_ascii=False, encoder='utf-8')


if __name__ == '__main__':
    fire.Fire()
