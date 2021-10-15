import fire
from httpx import get

# Settings
BASE_URL='https://swapi.dev/api/'


def people(name):
    "Returns a SW people."
    response = get(BASE_URL+'people/?search='+name).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])
        homeworld = get(response_dict['homeworld']).json()['name']

        vehicles = []
        for vehicle in response_dict['vehicles']:
            vehicle_itens = get(vehicle).json()['name']
            vehicles.append(vehicle_itens)

        films = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films.append(film_itens)

        starships = []
        for starship in response_dict['starships']:
            starship_itens = get(starship).json()['name']
            starships.append(starship_itens)

        character = {
            "Name": response_dict['name'],
            "Height (Meters)": int(response_dict['height'])/100,
            "Mass (Kg)": response_dict['mass'],
            "Hair Color": response_dict['hair_color'].capitalize(),
            "Skin Color": response_dict['skin_color'].capitalize(),
            "Birth Year": response_dict['birth_year'],
            "Gender": response_dict['gender'].capitalize(),
            "Homeworld": homeworld,
            "Films": films,
            "Vehicles": vehicles,
            "Starships": starships,
        }
        yield character


def planets(name):
    "Returns a SW planet."
    response = get(BASE_URL+'planets/?search='+name).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])

        residents = []
        for resident in response_dict['residents']:
            resident_itens = get(resident).json()['name']
            residents.append(resident_itens)

        films = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films.append(film_itens)

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
           "Residents": residents,
           "Films": films,
        }
        yield planet


if __name__ == '__main__':
    fire.Fire()
