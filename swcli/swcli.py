import fire
try:
    from swcli.render import Render
except:
    from render import Render


def films(id='', title=''):
    """
    Return a one or many movies on Star Wars trilogies by Title.
    """
    response = Render.show(id, title, 'films')
    return response


def people(id='', name=''):
    """
    Returns a character on the Star Wars movies.
    Like: Luke, Leia, Anakin, etc.
    """
    response = Render.show(id, name, 'people')
    return response


def planets(id='', name=''):
    """
    Return a planet.
    Like: Hoth, Naboo, etc.
    """
    response = Render.show(id, name, 'planets')
    return response


def species(id='', name=''):
    """
    Return a species on the Star Wars universe.
    Like: Wookie, Human, etc.
    """
    response = Render.show(id, name, 'species')
    return response


def starships(id='', name=''):
    """
    Return a Starships on Star Wars universe.
    Like: Death Star, Millenium Falcon, etc.
    """
    response = Render.show(id, name, 'starships')
    return response


def vehicles(id='', name=''):
    """
    Return a vehicle used on Star Wars universe.
    Like: TIE Fighter, Geonosian starfighter, etc.
    """
    response = Render.show(id, name, 'vehicles')
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
