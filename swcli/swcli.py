import fire
try:
    from swcli.models import Film
    from swcli.models import Person
    from swcli.models import Planet
    from swcli.models import Specie
    from swcli.models import Starship
    from swcli.models import Vehicle
except:
    from models import Film
    from models import Person
    from models import Planet
    from models import Specie
    from models import Starship
    from models import Vehicle


def films(id='', title=''):
    """
    Return a one or many movies on Star Wars trilogies by Title.
    """
    response = Film.get_film(id, title)
    return response


def people(id='', name=''):
    """
    Returns a character on the Star Wars movies.
    Like: Luke, Leia, Anakin, etc.
    """
    response = Person.get_person(id, name)
    return response


def planets(id='', name=''):
    """
    Return a planet.
    Like: Hoth, Naboo, etc.
    """
    response = Planet.get_planet(id, name)
    return response


def species(id='', name=''):
    """
    Return a species on the Star Wars universe.
    Like: Wookie, Human, etc.
    """
    response = Specie.get_specie(id, name)
    return response


def starships(id='', name=''):
    """
    Return a Starships on Star Wars universe.
    Like: Death Star, Millenium Falcon, etc.
    """
    response = Starship.get_starship(id, name)
    return response


def vehicles(id='', name=''):
    """
    Return a vehicle used on Star Wars universe.
    Like: TIE Fighter, Geonosian starfighter, etc.
    """
    response = Vehicle.get_vehicle(id, name)
    return response


def main():
    fire.Fire({
        'films': films,
        'people': people,
        'planets': planets,
        'species': species,
        'starships': starships,
        'vehicles': vehicles,
    })


if __name__ == '__main__':
    main()
