try:
    import swcli.settings as settings
    import swcli.utils as utils
    from swcli.models import Planet
except:
    import settings
    import utils
    from models import Planet
from httpx import get


class GetPlanet():
    def get_planet_by_id(planet_id):
        """
        Returns a planet on the Star Wars movies by searching ID.
        Like: Naboo, Coruscant, etc.
        """
        response = get(
            settings.BASE_URL +
            settings.PLANETS +
            str(planet_id))

        if response.status_code != 200:
            raise SystemExit('Resource does not exist!')

        json_data = response.json()

        planet_response = {
            "name": json_data['name'],
            "diameter": json_data['diameter'],
            "rotation_period": json_data['rotation_period'],
            "orbital_period": json_data['orbital_period'],
            "gravity": json_data['gravity'],
            "population": json_data['population'],
            "climate": json_data['climate'],
            "terrain": json_data['terrain'],
            "surface_water": json_data['surface_water'],
            "residents": utils.get_resources_dict(
                json_data['residents'],
                'name'),
            "films": utils.get_resources_dict(
                json_data['films'],
                'title'),
        }

        planet = Planet(**planet_response)
        yield planet.json(ensure_ascii=False, encoder='utf-8')

    def get_planets_by_name(name):
        """
        Returns a planet on the Star Wars movies by searching name.
        """
        json_data = get(
            settings.BASE_URL +
            settings.PLANETS +
            settings.SEARCH +
            name).json()

        if not json_data['results']:
            raise SystemExit('Resource does not exist!')

        for json_dict in json_data['results']:
            planet_response = {
                "name": json_dict['name'],
                "diameter": json_dict['diameter'],
                "rotation_period": json_dict['rotation_period'],
                "orbital_period": json_dict['orbital_period'],
                "gravity": json_dict['gravity'],
                "population": json_dict['population'],
                "climate": json_dict['climate'],
                "terrain": json_dict['terrain'],
                "surface_water": json_dict['surface_water'],
                "residents": utils.get_resources_dict(
                    json_dict['residents'],
                    'name'),
                "films": utils.get_resources_dict(
                    json_dict['films'],
                    'title'),
            }

        planet = Planet(**planet_response)
        yield planet.json(ensure_ascii=False, encoder='utf-8')
