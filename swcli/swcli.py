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

        film_response = {
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

        yield film_response


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

        character_response = {
            "Name": response_dict['name'],
            "Height (Meters)": int(response_dict['height'])/100,
            "Mass (Kg)": response_dict['mass'],
            "Hair Color": response_dict['hair_color'],
            "Skin Color": response_dict['skin_color'],
            "Birth Year": response_dict['birth_year'],
            "Gender": response_dict['gender'],
            "Homeworld": homeworld,
            "Films": films_list,
            "Vehicles": vehicles_list,
            "Starships": starships_list,
        }

        yield character_response


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

        planet_response = {
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

        yield planet_response


def species(name):
    "Return a SW specie."
    response = get(BASE_URL+'species/?search='+name).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])

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
            "Name": response_dict['name'],
            "Classification": response_dict['classification'],
            "Designation": response_dict['designation'],
            "Average Height (Meters)": int(response_dict['average_height'])/100,
            "Average Lifespan (Years)": response_dict['average_lifespan'],
            "Eye Colors": response_dict['eye_colors'],
            "Hair Colors": response_dict['hair_colors'],
            "Skin Colors": response_dict['skin_colors'],
            "Language": response_dict['language'],
            "Homeworld": homeworld,
            "People": people_list,
            "Films": films_list,
        }

        yield species_response


def starships(name):
    "Return a SW starship."
    response = get(BASE_URL+'starships/?search='+name).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])

        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        pilots_list = []
        for pilot in response_dict['pilots']:
            pilot_itens = get(pilot).json()['name']
            pilots_list.append(pilot_itens)

        starships_response = {
            "Name": response_dict['name'],
            "Model": response_dict['model'],
            "Starship Class": response_dict['starship_class'],
            "Manufacturer": response_dict['manufacturer'],
            "Cost (Credits)": response_dict['cost_in_credits'],
            "Length (Meters)": response_dict['length'],
            "Crew": response_dict['crew'],
            "Passengers": response_dict['passengers'],
            "Max Atmosphering Speed": response_dict['max_atmosphering_speed'],
            "Hyperdrive Rating": response_dict['hyperdrive_rating'],
            "MGLT": response_dict['MGLT'],
            "Cargo Capacity": response_dict['cargo_capacity'],
            "Consumables": response_dict['consumables'],
            "Films": films_list,
            "Pilots": pilots_list,
        }

        yield starships_response


def vehicles(name):
    "Return a SW vehicle."
    response = get(BASE_URL+'vehicles/?search='+name).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])

        films_list = []
        for film in response_dict['films']:
            film_itens = get(film).json()['title']
            films_list.append(film_itens)

        pilots_list = []
        for pilot in response_dict['pilots']:
            pilot_itens = get(pilot).json()['name']
            pilots_list.append(pilot_itens)

        vehicles_response = {
            "Name": response_dict['name'],
            "Model": response_dict['model'],
            "Vehicle Class": response_dict['vehicle_class'],
            "Manufacturer": response_dict['manufacturer'],
            "Length (Meters)": response_dict['length'],
            "Cost (Credits)": response_dict['cost_in_credits'],
            "Crew": response_dict['crew'],
            "Passengers": response_dict['passengers'],
            "Max Atmosphering Speed": response_dict['max_atmosphering_speed'],
            "Cargo Capacity (Kg)": response_dict['cargo_capacity'],
            "Consumables": response_dict['consumables'],
            "Films": films_list,
            "Pilots": pilots_list,
        }

        yield vehicles_response


if __name__ == '__main__':
    fire.Fire()
