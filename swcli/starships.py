try:
    import swcli.utils as utils
    from swcli.models import Starship
except:
    import utils
    from models import Starship
from httpx import get


class GetStarship(object):
    def get_starship_by_id(starship_id):
        """
        Return a one starship on Star Wars trilogies by ID.
        """
        starships_url = f'https://swapi.dev/api/starships/{starship_id}/'
        response = get(starships_url)

        if response.status_code != 200:
            raise SystemExit('Resource does not exist!')

        json_data = response.json()

        starships_response = {
            "name": json_data['name'],
            "model": json_data['model'],
            "starship_class": json_data['starship_class'],
            "manufacturer": json_data['manufacturer'],
            "cost": json_data['cost_in_credits'],
            "length": json_data['length'],
            "crew": json_data['crew'],
            "passengers": json_data['passengers'],
            "max_atmosphering_speed": json_data['max_atmosphering_speed'],
            "hyperdrive_rating": json_data['hyperdrive_rating'],
            "mglt": json_data['MGLT'],
            "cargo_capacity": json_data['cargo_capacity'],
            "consumables": json_data['consumables'],
            "films": utils.get_resources_dict(
                json_data['films'],
                'title'),
            "pilots": utils.get_resources_dict(
                json_data['pilots'],
                'name'),
        }

        starship = Starship(**starships_response)
        yield starship.json(ensure_ascii=False, encoder='utf-8')

    def get_starship_by_name(name):
        """
        Return a Starships on Star Wars universe.
        Like: Death Star, Millenium Falcon, etc.
        """
        starships_url = f'https://swapi.dev/api/starships/?search={name}'
        json_data = get(starships_url).json()

        if not json_data['results']:
            raise SystemExit('Resource does not exist!')

        for json_dict in json_data['results']:

            starships_response = {
                "name": json_dict['name'],
                "model": json_dict['model'],
                "starship_class": json_dict['starship_class'],
                "manufacturer": json_dict['manufacturer'],
                "cost": json_dict['cost_in_credits'],
                "length": json_dict['length'],
                "crew": json_dict['crew'],
                "passengers": json_dict['passengers'],
                "max_atmosphering_speed": json_dict['max_atmosphering_speed'],
                "hyperdrive_rating": json_dict['hyperdrive_rating'],
                "mglt": json_dict['MGLT'],
                "cargo_capacity": json_dict['cargo_capacity'],
                "consumables": json_dict['consumables'],
                "films": utils.get_resources_dict(
                    json_dict['films'],
                    'title'),
                "pilots": utils.get_resources_dict(
                    json_dict['pilots'],
                    'name'),
            }

            starship = Starship(**starships_response)
            yield starship.json(ensure_ascii=False, encoder='utf-8')
