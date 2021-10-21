import settings
import utils
from httpx import get
from models import Film


class GetFilm():
    def get_film_by_id(film_id):
        response = get(
            settings.BASE_URL +
            settings.FILMS +
            str(film_id)).json()

        film_response = {
            "title": response['title'],
            "episode": response['episode_id'],
            "director": response['director'],
            "producer": response['producer'],
            "release_date": response['release_date'],
            "species": utils.get_resources_dict(
                response['species'],
                'name'),
            "starships": utils.get_resources_dict(
                response['starships'],
                'name'),
            "vehicles": utils.get_resources_dict(
                response['vehicles'],
                'name'),
            "characters": utils.get_resources_dict(
                response['characters'],
                'name'),
            "planets": utils.get_resources_dict(
                response['planets'],
                'name'),
        }
        film = Film(**film_response)
        yield film.json(ensure_ascii=False, encoder='utf-8')

    def get_film_by_title(title):
        """
        Return a one or many movies on Star Wars trilogies by Title.
        """
        response = get(
            settings.BASE_URL +
            settings.FILMS +
            settings.SEARCH +
            title).json()

        for response_dict in response['results']:
            film_response = {
                "title": response_dict['title'],
                "episode": response_dict['episode_id'],
                "director": response_dict['director'],
                "producer": response_dict['producer'],
                "release_date": response_dict['release_date'],
                "species": utils.get_resources_dict(
                    response_dict['species'],
                    'name'),
                "starships": utils.get_resources_dict(
                    response_dict['starships'],
                    'name'),
                "vehicles": utils.get_resources_dict(
                    response_dict['vehicles'],
                    'name'),
                "characters": utils.get_resources_dict(
                    response_dict['characters'],
                    'name'),
                "planets": utils.get_resources_dict(
                    response_dict['planets'],
                    'name'),
            }

            film = Film(**film_response)
            yield film.json(ensure_ascii=False, encoder='utf-8')
