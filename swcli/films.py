try:
    import swcli.utils as utils
    from swcli.models import Film
except:
    import utils
    from models import Film
from httpx import get


class GetFilm():
    def get_film_by_id(film_id):
        """
        Return a one or many movies on Star Wars trilogies by ID.
        """
        films_url = f'https://swapi.dev/api/films/{film_id}/'
        response = get(films_url)

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
        films_url = f'https://swapi.dev/api/films/?search={title}'
        json_data = get(films_url).json()

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
