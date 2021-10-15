import fire
from httpx import get

# Settings
BASE_URL='https://swapi.dev/api/'


def films(title):
    "Returns a SW film"
    response = get(BASE_URL+'films/?search='+title).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])

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

        film = {
            "Title": response_dict['title'],
            "Episode": response_dict['episode_id'],
            "Opening Crawl": response_dict['opening_crawl'],
            "Director": response_dict['director'],
            "Producer": response_dict['producer'],
            "Release Data": response_dict['release_date'],
            "Species": species_list,
            "Starships": starships_list,
            "Vehicles": vehicles_list,
            "Characters": characters_list,
            "Planets": planets_list,
        }
        yield film


def people(name):
    "Returns a SW people."
    response = get(BASE_URL+'people/?search='+name).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])
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

        character = {
            "Name": response_dict['name'],
            "Height (Meters)": int(response_dict['height'])/100,
            "Mass (Kg)": response_dict['mass'],
            "Hair Color": response_dict['hair_color'].capitalize(),
            "Skin Color": response_dict['skin_color'].capitalize(),
            "Birth Year": response_dict['birth_year'],
            "Gender": response_dict['gender'].capitalize(),
            "Homeworld": homeworld,
            "Films": films_list,
            "Vehicles": vehicles_list,
            "Starships": starships_list,
        }
        yield character


def planets(name):
    "Returns a SW planet."
    response = get(BASE_URL+'planets/?search='+name).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])

        residents_list = []
        for resident in response_dict['residents']:
            resident_itens = get(resident).json()['name']
            residents_list.append(resident_itens)

        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        planet = {
           "Name": response_dict['name'],
           "Diameter (Km)": response_dict['diameter'],
           "Rotation Period (Hours)": response_dict['rotation_period'],
           "Orbital Period (Days)": response_dict['orbital_period'],
           "Gravity (G)": response_dict['gravity'],
           "Population": response_dict['population'],
           "Climate": response_dict['climate'],
           "Terrain": response_dict['terrain'],
           "Surface Water": response_dict['surface_water'],
           "Residents": residents_list,
           "Films": films_list,
        }
        yield planet


if __name__ == '__main__':
    fire.Fire()
