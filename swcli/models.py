try:
    import swcli.utils as utils
except:
    import utils
from pydantic import BaseModel
from typing import List
from httpx import get


class Film(BaseModel):
    title: str
    episode: str
    director: str
    producer: str
    release_date: str
    species: List[str]
    starships: List[str]
    vehicles: List[str]
    characters: List[str]
    planets: List[str]

    def get_film(film_id, film_title):
        """
        Returns a film by searching by ID or name.
        """
        try:
            if film_id and not film_title:
                json_data = utils.query_by_id(film_id, 'films')
            elif not film_id and film_title:
                json_data = utils.query_by_name(film_title, 'films')

            for resource in json_data:
                species = utils.get_resources_dict(
                    resource['species'],
                    'name')
                starships = utils.get_resources_dict(
                    resource['starships'],
                    'name')
                vehicles = utils.get_resources_dict(
                    resource['vehicles'],
                    'name')
                characters = utils.get_resources_dict(
                    resource['characters'],
                    'name')
                planets = utils.get_resources_dict(
                    resource['planets'],
                    'name')
                film_response = {
                    "title": resource['title'],
                    "episode": resource['episode_id'],
                    "director": resource['director'],
                    "producer": resource['producer'],
                    "release_date": resource['release_date'],
                    "species": species,
                    "starships": starships,
                    "vehicles": vehicles,
                    "characters": characters,
                    "planets": planets,
                }

                film = Film(**film_response)
                yield film.json(ensure_ascii=False, encoder='utf-8')
        except BaseException:
            raise SystemExit('Invalid search or Resource does not exist!')


class Person(BaseModel):
    name: str
    height: float
    mass: str
    hair_color: str
    skin_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    vehicles: List[str]
    starships: List[str]

    def get_person(person_id, person_name):
        """
        Returns a character on the Star Wars movies by searching by ID or name.
        """
        try:
            if person_id and not person_name:
                json_data = utils.query_by_id(person_id, 'people')
            elif not person_id and person_name:
                json_data = utils.query_by_name(person_name, 'people')

            for resource in json_data:
                homeworld = get(resource['homeworld']).json()['name']
                films = utils.get_resources_dict(resource['films'], 'title')
                vehicles = utils.get_resources_dict(
                    resource['vehicles'], 'name')
                starships = utils.get_resources_dict(
                    resource['starships'], 'name')
                character_response = {
                    "name": resource['name'],
                    "height": int(
                        resource['height']) / 100,
                    "mass": resource['mass'],
                    "hair_color": resource['hair_color'],
                    "skin_color": resource['skin_color'],
                    "birth_year": resource['birth_year'],
                    "gender": resource['gender'],
                    "homeworld": homeworld,
                    "films": films,
                    "vehicles": vehicles,
                    "starships": starships,
                }

                person = Person(**character_response)
                yield person.json(ensure_ascii=False, encoder='utf-8')
        except BaseException:
            raise SystemExit('Invalid search or Resource does not exist!')


class Planet(BaseModel):
    name: str
    diameter: int
    rotation_period: int
    orbital_period: int
    gravity: str
    population: int
    climate: str
    terrain: str
    surface_water: str
    residents: List[str]
    films: List[str]

    def get_planet(planet_id, planet_name):
        """
        Returns a planet on the Star Wars movies by searching by ID or name.
        """
        try:
            if planet_id and not planet_name:
                json_data = utils.query_by_id(planet_id, 'planets')
            elif not planet_id and planet_name:
                json_data = utils.query_by_name(planet_name, 'planets')

            for resource in json_data:
                residents = utils.get_resources_dict(
                    resource['residents'],
                    'name')
                films = utils.get_resources_dict(
                    resource['films'],
                    'title')
                planet_response = {
                    "name": resource['name'],
                    "diameter": resource['diameter'],
                    "rotation_period": resource['rotation_period'],
                    "orbital_period": resource['orbital_period'],
                    "gravity": resource['gravity'],
                    "population": resource['population'],
                    "climate": resource['climate'],
                    "terrain": resource['terrain'],
                    "surface_water": resource['surface_water'],
                    "residents": residents,
                    "films": films,
                }

                planet = Planet(**planet_response)
                yield planet.json(ensure_ascii=False, encoder='utf-8')
        except BaseException:
            raise SystemExit('Invalid search or Resource does not exist!')


class Specie(BaseModel):
    name: str
    classification: str
    designation: str
    average_height: str
    average_lifespan: str
    eye_colors: str
    hair_colors: str
    skin_colors: str
    language: str
    homeworld: str
    people: List[str]
    films: List[str]

    def get_specie(specie_id, specie_name):
        """
        Returns a specie on the Star Wars movies by searching by ID or name.
        """
        try:
            if specie_id and not specie_name:
                json_data = utils.query_by_id(specie_id, 'species')
            elif not specie_id and specie_name:
                json_data = utils.query_by_name(specie_name, 'species')

            for resource in json_data:
                homeworld = get(resource['homeworld']).json()['name']
                people = utils.get_resources_dict(
                    resource['people'],
                    'name')
                films = utils.get_resources_dict(
                    resource['films'],
                    'title')
                species_response = {
                    "name": resource['name'],
                    "classification": resource['classification'],
                    "designation": resource['designation'],
                    "average_height": int(resource['average_height']) / 100,
                    "average_lifespan": resource['average_lifespan'],
                    "eye_colors": resource['eye_colors'],
                    "hair_colors": resource['hair_colors'],
                    "skin_colors": resource['skin_colors'],
                    "language": resource['language'],
                    "homeworld": homeworld,
                    "people": people,
                    "films": films,
                }

                specie = Specie(**species_response)
                yield specie.json(ensure_ascii=False, encoder='utf-8')
        except BaseException:
            raise SystemExit('Invalid search or Resource does not exist!')


class Starship(BaseModel):
    name: str
    model: str
    starship_class: str
    manufacturer: str
    cost: str
    length: str
    crew: str
    passengers: str
    max_atmosphering_speed: str
    hyperdrive_rating: str
    mglt: str
    cargo_capacity: str
    consumables: str
    films: List[str]
    pilots: List[str]

    def get_starship(starship_id, starship_name):
        """
        Returns a specie on the Star Wars movies by searching by ID or name.
        """
        try:
            if starship_id and not starship_name:
                json_data = utils.query_by_id(starship_id, 'starships')
            elif not starship_id and starship_name:
                json_data = utils.query_by_name(starship_name, 'starships')

            for resource in json_data:
                films = utils.get_resources_dict(
                    resource['films'],
                    'title')
                pilots = utils.get_resources_dict(
                    resource['pilots'],
                    'name')
                starships_response = {
                    "name": resource['name'],
                    "model": resource['model'],
                    "starship_class": resource['starship_class'],
                    "manufacturer": resource['manufacturer'],
                    "cost": resource['cost_in_credits'],
                    "length": resource['length'],
                    "crew": resource['crew'],
                    "passengers": resource['passengers'],
                    "max_atmosphering_speed": resource['max_atmosphering_speed'],
                    "hyperdrive_rating": resource['hyperdrive_rating'],
                    "mglt": resource['MGLT'],
                    "cargo_capacity": resource['cargo_capacity'],
                    "consumables": resource['consumables'],
                    "films": films,
                    "pilots": pilots,
                }

                starship = Starship(**starships_response)
                yield starship.json(ensure_ascii=False, encoder='utf-8')
        except BaseException:
            raise SystemExit('Invalid search or Resource does not exist!')


class Vehicle(BaseModel):
    name: str
    model: str
    vehicle_class: str
    manufacturer: str
    length: str
    cost: str
    crew: str
    passengers: str
    max_atmosphering_speed: str
    cargo_capacity: str
    consumables: str
    films: List[str]
    pilots: List[str]

    def get_vehicle(vehicle_id, vehicle_name):
        """
        Returns a vehicle on the Star Wars movies by searching by ID or name.
        """
        try:
            if vehicle_id and not vehicle_name:
                json_data = utils.query_by_id(vehicle_id, 'vehicles')
            elif not vehicle_id and vehicle_name:
                json_data = utils.query_by_name(vehicle_name, 'vehicles')

            for resource in json_data:
                films = utils.get_resources_dict(
                    resource['films'],
                    'title')
                pilots = utils.get_resources_dict(
                    resource['pilots'],
                    'name')

                vehicles_response = {
                    "name": resource['name'],
                    "model": resource['model'],
                    "vehicle_class": resource['vehicle_class'],
                    "manufacturer": resource['manufacturer'],
                    "length": resource['length'],
                    "cost": resource['cost_in_credits'],
                    "crew": resource['crew'],
                    "passengers": resource['passengers'],
                    "max_atmosphering_speed": resource['max_atmosphering_speed'],
                    "cargo_capacity": resource['cargo_capacity'],
                    "consumables": resource['consumables'],
                    "films": films,
                    "pilots": pilots,
                }

                vehicle = Vehicle(**vehicles_response)
                yield vehicle.json(ensure_ascii=False, encoder='utf-8')
        except BaseException:
            raise SystemExit('Invalid search or Resource does not exist!')
