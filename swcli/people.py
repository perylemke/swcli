try:
    import swcli.settings as settings
    import swcli.utils as utils
    from swcli.models import Person
except:
    import settings
    import utils
    from models import Person
from httpx import get


class GetPerson():
    def get_person_by_id(person_id):
        """
        Returns a character on the Star Wars movies by searching ID.
        Like: Luke, Leia, Anakin, etc.
        """
        response = get(
            settings.BASE_URL +
            settings.PEOPLE +
            str(person_id))

        if response.status_code != 200:
            raise SystemExit('Resource does not exist!')

        json_data = response.json()

        homeworld = get(json_data['homeworld']).json()['name']

        character_response = {
            "name": json_data['name'],
            "height": int(
                json_data['height']) / 100,
            "mass": json_data['mass'],
            "hair_color": json_data['hair_color'],
            "skin_color": json_data['skin_color'],
            "birth_year": json_data['birth_year'],
            "gender": json_data['gender'],
            "homeworld": homeworld,
            "films": utils.get_resources_dict(
                json_data['films'],
                'title'),
            "vehicles": utils.get_resources_dict(
                json_data['vehicles'],
                'name'),
            "starships": utils.get_resources_dict(
                json_data['starships'],
                'name'),
        }

        person = Person(**character_response)
        yield person.json(ensure_ascii=False, encoder='utf-8')

    def get_person_by_name(name):
        """
        Returns a character on the Star Wars movies by searching name.
        """
        json_data = get(
            settings.BASE_URL +
            settings.PEOPLE +
            settings.SEARCH +
            name).json()

        if not json_data['results']:
            raise SystemExit('Resource does not exist!')

        for json_dict in json_data['results']:
            homeworld = get(json_dict['homeworld']).json()['name']

            character_response = {
                "name": json_dict['name'],
                "height": int(
                    json_dict['height']) / 100,
                "mass": json_dict['mass'],
                "hair_color": json_dict['hair_color'],
                "skin_color": json_dict['skin_color'],
                "birth_year": json_dict['birth_year'],
                "gender": json_dict['gender'],
                "homeworld": homeworld,
                "films": utils.get_resources_dict(
                    json_dict['films'],
                    'title'),
                "vehicles": utils.get_resources_dict(
                    json_dict['vehicles'],
                    'name'),
                "starships": utils.get_resources_dict(
                    json_dict['starships'],
                    'name'),
            }

            person = Person(**character_response)
            yield person.json(ensure_ascii=False, encoder='utf-8')
