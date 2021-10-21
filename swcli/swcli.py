import fire
import settings
from httpx import get
from models import Specie, Starship, Vehicle
from films import GetFilm
from people import GetPerson
from planets import GetPlanet


def films(id='', title=''):
    """
    Return a one or many movies on Star Wars trilogies by Title.
    """
    if id != '':
        response = GetFilm.get_film_by_id(id)
    elif title != '':
        response = GetFilm.get_film_by_title(title)

    return response


def people(id='', name=''):
    """
    Returns a character on the Star Wars movies.
    Like: Luke, Leia, Anakin, etc.
    """
    if id != '':
        response = GetPerson.get_person_by_id(id)
    elif name != '':
        response = GetPerson.get_person_by_name(name)

    return response


def planets(id='', name=''):
    """
    Return a planet.
    Like: Hoth, Naboo, etc.
    """
    if id != '':
        response = GetPlanet.get_planet_by_id(id)
    elif name != '':
        response = GetPlanet.get_planets_by_name(name)

    return response


def species(name):
    """
    Return a species on the Star Wars universe.
    Like: Wookie, Human, etc.
    """
    response = get(
        settings.BASE_URL +
        settings.SPECIES +
        settings.SEARCH +
        name).json()

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
            "average_height": int(response_dict['average_height']) / 100,
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
    """
    Return a Starships on Star Wars universe.
    Like: Death Star, Millenium Falcon, etc.
    """
    response = get(
        settings.BASE_URL +
        settings.STARSHIPS +
        settings.SEARCH +
        name).json()

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
    """
    Return a vehicle used on Star Wars universe.
    Like: TIE Fighter, Geonosian starfighter, etc.
    """
    response = get(
        settings.BASE_URL +
        settings.VEHICLES +
        settings.SEARCH +
        name).json()

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
    fire.Fire({
        'films': films,
        'people': people,
        'planets': planets,
        'species': species,
        'starships': starships,
        'vehicles': vehicles,
    })
