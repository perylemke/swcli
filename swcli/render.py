try:
    import swcli.utils as utils
    from swcli.exceptions import (
        InvalidSearchError,
        ResourceDoesNotExistError,
    )
except:
    import utils
    from exceptions import InvalidSearchError, ResourceDoesNotExistError
from httpx import get


class Render(object):
    def show(resource_id, resource_name, resource_type):
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
                    if label in ('Created', 'Edited', 'Url'):
                        pass
                    elif label == 'Homeworld':
                        homeworld = get(json_dict['homeworld']).json()['name']
                        print(f'{label}: {homeworld}')
                    elif label == 'Height':
                        height = int(json_dict['height']) / 100
                        print(f'{label}: {height}')
                    elif label == 'Films':
                        films = utils.get_resources_dict(
                            json_dict['films'],
                            'title')
                        print(f'{label}: {films}')
                    elif label in ('Species',
                                   'Vehicles',
                                   'Starships',
                                   'Characters',
                                   'Planets',
                                   'Residents',
                                   'People',
                                   'Pilots'):
                        special_label = utils.get_resources_dict(
                            json_dict[label.lower()],
                            'name')
                        print(f'{label}: {special_label}')
                    else:
                        print(f'{label}: {json_dict[json_data]}')
                print('')
        except InvalidSearchError as e:
            raise SystemExit(e)
        except ResourceDoesNotExistError as e:
            raise SystemExit(e)
