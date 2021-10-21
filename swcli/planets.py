import settings
import utils
from httpx import get
from models import Planet


class GetPlanet():
    def get_planet_by_id(planet_id):
        """
        Returns a planet on the Star Wars movies by searching ID.
        Like: Naboo, Coruscant, etc.
        """
        response = get(
            settings.BASE_URL +
            settings.PLANETS +
            str(planet_id)).json()

        planet_response = {
            "name": response['name'],
            "diameter": response['diameter'],
            "rotation_period": response['rotation_period'],
            "orbital_period": response['orbital_period'],
            "gravity": response['gravity'],
            "population": response['population'],
            "climate": response['climate'],
            "terrain": response['terrain'],
            "surface_water": response['surface_water'],
            "residents": utils.get_resources_dict(
                response['residents'],
                'name'),
            "films": utils.get_resources_dict(
                response['films'],
                'title'),
        }

        planet = Planet(**planet_response)
        yield planet.json(ensure_ascii=False, encoder='utf-8')

    def get_planets_by_name(name):
        """
        Returns a planet on the Star Wars movies by searching name.
        """
        response = get(
            settings.BASE_URL +
            settings.PLANETS +
            settings.SEARCH +
            name).json()

        for response_dict in response['results']:
            planet_response = {
                "name": response_dict['name'],
                "diameter": response_dict['diameter'],
                "rotation_period": response_dict['rotation_period'],
                "orbital_period": response_dict['orbital_period'],
                "gravity": response_dict['gravity'],
                "population": response_dict['population'],
                "climate": response_dict['climate'],
                "terrain": response_dict['terrain'],
                "surface_water": response_dict['surface_water'],
                "residents": utils.get_resources_dict(
                    response_dict['residents'],
                    'name'),
                "films": utils.get_resources_dict(
                    response_dict['films'],
                    'title'),
            }

        planet = Planet(**planet_response)
        yield planet.json(ensure_ascii=False, encoder='utf-8')
