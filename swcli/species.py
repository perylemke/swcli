try:
    import swcli.settings as settings
    import swcli.utils as utils
    from swcli.models import Planet
except:
    import settings
    import utils
    from models import Planet
from httpx import get


class GetSpecie(object):
    def get_specie_by_id(specie_id):
        """
        Return a one or many species on Star Wars trilogies by ID.
        """
        response = get(
            settings.BASE_URL +
            settings.SPECIES +
            str(specie_id))

        if response.status_code != 200:
            raise SystemExit('Resource does not exist!')

        json_data = response.json()

        homeworld = get(json_data['homeworld']).json()['name']

        species_response = {
            "name": json_data['name'],
            "classification": json_data['classification'],
            "designation": json_data['designation'],
            "average_height": int(json_data['average_height']) / 100,
            "average_lifespan": json_data['average_lifespan'],
            "eye_colors": json_data['eye_colors'],
            "hair_colors": json_data['hair_colors'],
            "skin_colors": json_data['skin_colors'],
            "language": json_data['language'],
            "homeworld": homeworld,
            "people": utils.get_resources_dict(
                json_data['people'],
                'name'),
            "films": utils.get_resources_dict(
                json_data['films'],
                'title'),
        }

        specie = Specie(**species_response)
        yield specie.json(ensure_ascii=False, encoder='utf-8')

    def get_specie_by_name(name):
        """
        Returns a specie on the Star Wars movies by searching name.
        """
        json_data = get(
            settings.BASE_URL +
            settings.SPECIES +
            settings.SEARCH +
            name).json()

        if not json_data['results']:
            raise SystemExit('Resource does not exist!')

        for json_dict in json_data['results']:
            homeworld = get(json_dict['homeworld']).json()['name']

            species_response = {
                "name": json_dict['name'],
                "classification": json_dict['classification'],
                "designation": json_dict['designation'],
                "average_height": int(json_dict['average_height']) / 100,
                "average_lifespan": json_dict['average_lifespan'],
                "eye_colors": json_dict['eye_colors'],
                "hair_colors": json_dict['hair_colors'],
                "skin_colors": json_dict['skin_colors'],
                "language": json_dict['language'],
                "homeworld": homeworld,
                "people": utils.get_resources_dict(
                    json_dict['people'],
                    'name'),
                "films": utils.get_resources_dict(
                    json_dict['films'],
                    'title'),
            }

        specie = Specie(**species_response)
        yield specie.json(ensure_ascii=False, encoder='utf-8')
