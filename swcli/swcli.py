import fire
from httpx import get


def people(name):
    "Returns a SW people."
    BASE_URL='https://swapi.dev/api/people/?search={name}'

    response = get(BASE_URL.format(name=name)).json()

    for number in range(len(response['results'])):
        response_dict = dict(response['results'][number])
        homeworld = get(response_dict['homeworld']).json()['name']

        vehicles = []
        for i in response_dict['vehicles']:
            vehicle = get(i).json()['name']
            vehicles.append(vehicle)

        films = []
        for f in response_dict['films']:
            film = get(f).json()['title']
            films.append(film)

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
        }
        return character


if __name__ == '__main__':
    fire.Fire()
