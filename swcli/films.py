import settings
import utils
from httpx import get
from models import Film


class GetFilm():
    def get_film_by_id(film_id):
        """
        Return a one or many movies on Star Wars trilogies by ID.
        """
        response = get(
            settings.BASE_URL +
            settings.FILMS +
            str(film_id))

        if response.status_code != 200:
            raise SystemExit('Resource does not exist!')

        json_data = response.json()

        film_response = {
            "title": json_data['title'],
            "episode": json_data['episode_id'],
            "director": json_data['director'],
            "producer": json_data['producer'],
            "release_date": json_data['release_date'],
            "species": utils.get_resources_dict(
                json_data['species'],
                'name'),
            "starships": utils.get_resources_dict(
                json_data['starships'],
                'name'),
            "vehicles": utils.get_resources_dict(
                json_data['vehicles'],
                'name'),
            "characters": utils.get_resources_dict(
                json_data['characters'],
                'name'),
            "planets": utils.get_resources_dict(
                json_data['planets'],
                'name'),
        }
        film = Film(**film_response)
        yield film.json(ensure_ascii=False, encoder='utf-8')

    def get_film_by_title(title):
        """
        Return a one or many movies on Star Wars trilogies by Title.
        """
        json_data = get(
            settings.BASE_URL +
            settings.FILMS +
            settings.SEARCH +
            title).json()

        if not json_data['results']:
            raise SystemExit('Resource does not exist!')

        for json_dict in json_data['results']:
            film_response = {
                "title": json_dict['title'],
                "episode": json_dict['episode_id'],
                "director": json_dict['director'],
                "producer": json_dict['producer'],
                "release_date": json_dict['release_date'],
                "species": utils.get_resources_dict(
                    json_dict['species'],
                    'name'),
                "starships": utils.get_resources_dict(
                    json_dict['starships'],
                    'name'),
                "vehicles": utils.get_resources_dict(
                    json_dict['vehicles'],
                    'name'),
                "characters": utils.get_resources_dict(
                    json_dict['characters'],
                    'name'),
                "planets": utils.get_resources_dict(
                    json_dict['planets'],
                    'name'),
            }

            film = Film(**film_response)
            yield film.json(ensure_ascii=False, encoder='utf-8')
