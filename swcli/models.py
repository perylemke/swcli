from pydantic import BaseModel
from typing import List


class _Film(BaseModel):
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


class _Person(BaseModel):
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


class _Planet(BaseModel):
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


class _Specie(BaseModel):
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


class _Starship(BaseModel):
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


class _Vehicle(BaseModel):
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
