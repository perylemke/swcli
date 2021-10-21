import settings
import utils
from httpx import get
from models import Person


class GetPerson():
    def get_person_by_id(person_id):
        """
        Returns a character on the Star Wars movies by searching ID.
        Like: Luke, Leia, Anakin, etc.
        """
        response = get(
            settings.BASE_URL +
            settings.PEOPLE +
            str(person_id)).json()

        homeworld = get(response['homeworld']).json()['name']

        character_response = {
            "name": response['name'],
            "height": int(
                response['height']) / 100,
            "mass": response['mass'],
            "hair_color": response['hair_color'],
            "skin_color": response['skin_color'],
            "birth_year": response['birth_year'],
            "gender": response['gender'],
            "homeworld": homeworld,
            "films": utils.get_resources_dict(
                response['films'],
                'title'),
            "vehicles": utils.get_resources_dict(
                response['vehicles'],
                'name'),
            "starships": utils.get_resources_dict(
                response['starships'],
                'name'),
        }

        person = Person(**character_response)
        yield person.json(ensure_ascii=False, encoder='utf-8')

    def get_person_by_name(name):
        """
        Returns a character on the Star Wars movies by searching name.
        """
        response = get(
            settings.BASE_URL +
            settings.PEOPLE +
            settings.SEARCH +
            name).json()

        for response_dict in response['results']:
            homeworld = get(response_dict['homeworld']).json()['name']

            character_response = {
                "name": response_dict['name'],
                "height": int(
                    response_dict['height']) / 100,
                "mass": response_dict['mass'],
                "hair_color": response_dict['hair_color'],
                "skin_color": response_dict['skin_color'],
                "birth_year": response_dict['birth_year'],
                "gender": response_dict['gender'],
                "homeworld": homeworld,
                "films": utils.get_resources_dict(
                    response_dict['films'],
                    'title'),
                "vehicles": utils.get_resources_dict(
                    response_dict['vehicles'],
                    'name'),
                "starships": utils.get_resources_dict(
                    response_dict['starships'],
                    'name'),
            }

            person = Person(**character_response)
            yield person.json(ensure_ascii=False, encoder='utf-8')
