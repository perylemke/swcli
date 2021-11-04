try:
    import swcli.utils as utils
    from swcli.exceptions import InvalidSearchError, ResourceDoesNotExistError
except:
    import utils
    from exceptions import InvalidSearchError, ResourceDoesNotExistError
from httpx import get


def render(resource_id, resource_name, resource_type):
    try:
        if resource_id and not resource_name:
            json_list = utils.query_by_id(resource_id, resource_type)
        elif not resource_id and resource_name:
            json_list = utils.query_by_name(resource_name, resource_type)
        else:
            raise InvalidSearchError("Invalid search!")

        for json_dict in json_list:
            for json_data in json_dict:
                label = json_data.capitalize().replace('_', ' ')
                if label == 'Created' or label == 'Edited' or label == 'Url':
                    pass
                elif label == 'Homeworld':
                    homeworld = get(json_dict['homeworld']).json()['name']
                    print(f'{label}: {homeworld}')
                elif label == 'Height':
                    height = int(json_dict['height'])/100
                    print(f'{label}: {height}')
                elif label == 'Films':
                    films = utils.get_resources_dict(
                        json_dict['films'],
                        'title')
                    print(f'{label}: {films}')
                elif label == 'Species':
                    species = utils.get_resources_dict(
                        json_dict['species'],
                        'name')
                    print(f'{label}: {species}')
                elif label == 'Vehicles':
                    vehicles = utils.get_resources_dict(
                        json_dict['vehicles'],
                        'name')
                    print(f'{label}: {vehicles}')
                elif label == 'Starships':
                    starships = utils.get_resources_dict(
                        json_dict['starships'],
                        'name')
                    print(f'{label}: {starships}')
                elif label == 'Characters':
                    characters = utils.get_resources_dict(
                        json_dict['characters'],
                        'name')
                    print(f'{label}: {characters}')
                elif label == 'Planets':
                    planets = utils.get_resources_dict(
                        json_dict['planets'],
                        'name')
                    print(f'{label}: {planets}')
                elif label == 'Residents':
                    residents = utils.get_resources_dict(
                        json_dict['residents'],
                        'name')
                    print(f'{label}: {residents}')
                elif label == 'People':
                    people = utils.get_resources_dict(
                        json_dict['people'],
                        'name')
                    print(f'{label}: {people}')
                elif label == 'Pilots':
                    pilots = utils.get_resources_dict(
                        json_dict['pilots'],
                        'name')
                    print(f'{label}: {pilots}')
                else:
                    print(f'{label}: {json_dict[json_data]}')
            print('')
    except InvalidSearchError as e:
        raise SystemExit(e)
    except ResourceDoesNotExistError as e:
        raise SystemExit(e)
