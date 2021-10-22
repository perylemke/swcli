import fire
from films import GetFilm
from people import GetPerson
from planets import GetPlanet
from species import GetSpecie
from starships import GetStarship
from vehicles import GetVehicle


def films(id='', title=''):
    """
    Return a one or many movies on Star Wars trilogies by Title.
    """
    if id != '' and title == '':
        response = GetFilm.get_film_by_id(id)
    elif title != '' and id == '':
        response = GetFilm.get_film_by_title(title)

    try:
        return response
    except BaseException:
        raise SystemExit('Invalid search!')


def people(id='', name=''):
    """
    Returns a character on the Star Wars movies.
    Like: Luke, Leia, Anakin, etc.
    """
    if id != '' and name == '':
        response = GetPerson.get_person_by_id(id)
    elif name != '' and id == '':
        response = GetPerson.get_person_by_name(name)

    try:
        return response
    except BaseException:
        raise SystemExit('Invalid search!')


def planets(id='', name=''):
    """
    Return a planet.
    Like: Hoth, Naboo, etc.
    """
    if id != '' and name == '':
        response = GetPlanet.get_planet_by_id(id)
    elif name != '' and id == '':
        response = GetPlanet.get_planets_by_name(name)

    try:
        return response
    except BaseException:
        raise SystemExit('Invalid search!')


def species(id='', name=''):
    """
    Return a species on the Star Wars universe.
    Like: Wookie, Human, etc.
    """
    if id != '' and name == '':
        response = GetSpecie.get_specie_by_id(id)
    elif name != '' and id == '':
        response = GetSpecie.get_specie_by_name(name)

    try:
        return response
    except BaseException:
        raise SystemExit('Invalid search!')


def starships(id='', name=''):
    """
    Return a Starships on Star Wars universe.
    Like: Death Star, Millenium Falcon, etc.
    """
    if id != '' and name == '':
        response = GetStarship.get_starship_by_id(id)
    elif name != '' and id == '':
        response = GetStarship.get_starship_by_name(name)

    try:
        return response
    except BaseException:
        raise SystemExit('Invalid search!')


def vehicles(id='', name=''):
    """
    Return a vehicle used on Star Wars universe.
    Like: TIE Fighter, Geonosian starfighter, etc.
    """
    if id != '' and name == '':
        response = GetVehicle.get_vehicle_by_id(id)
    elif name != '' and id == '':
        response = GetVehicle.get_vehicle_by_name(name)

    try:
        return response
    except BaseException:
        raise SystemExit('Invalid search!')


if __name__ == '__main__':
    fire.Fire({
        'films': films,
        'people': people,
        'planets': planets,
        'species': species,
        'starships': starships,
        'vehicles': vehicles,
    })
