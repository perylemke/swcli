import fire
try:
    from swcli.render import render
except:
    from render import render


def films(id='', title=''):
    """
    Return a one or many movies on Star Wars trilogies by Title.
    """
    response = render(id, title, 'films')
    return response


def people(id='', name=''):
    """
    Returns a character on the Star Wars movies.
    Like: Luke, Leia, Anakin, etc.
    """
    response = render(id, name, 'people')
    return response


def planets(id='', name=''):
    """
    Return a planet.
    Like: Hoth, Naboo, etc.
    """
    response = render(id, name, 'planets')
    return response


def species(id='', name=''):
    """
    Return a species on the Star Wars universe.
    Like: Wookie, Human, etc.
    """
    response = render(id, name, 'species')
    return response


def starships(id='', name=''):
    """
    Return a Starships on Star Wars universe.
    Like: Death Star, Millenium Falcon, etc.
    """
    response = render(id, name, 'starships')
    return response


def vehicles(id='', name=''):
    """
    Return a vehicle used on Star Wars universe.
    Like: TIE Fighter, Geonosian starfighter, etc.
    """
    response = render(id, name, 'vehicles')
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
