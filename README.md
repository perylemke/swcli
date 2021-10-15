# Star Wars CLI (swcli)

This CLI give the possibility to do a queries in [Star Wars API](https://swapi.dev/documentation) and returns a JSON in a terminal.

## Install

```
$ pip install swcli
```

## Queries Objects

- films
- people
- planets
- species
- starships
- vehicles

Ever object you can search by the name. Like below:

```
$ python3 swcli/swcli.py people --name=Luke
{"Name": "Luke Skywalker", "Height (Meters)": 1.72, "Mass (Kg)": "77", "Hair Color": "blond", "Skin Color": "fair", "Birth Year": "19BBY", "Gender": "male", "Homeworld": "Tatooine", "Films": ["A New Hope", "The Empire Strikes Back", "Return of the Jedi", "Revenge of the Sith"], "Vehicles": ["Snowspeeder", "Imperial Speeder Bike"], "Starships": ["X-wing", "Imperial shuttle"]}
```

## Tools and Libs

- Python 3.8
- Poetry
- Fire
- httpx
- PyTest

# Improvements

- Refactoring
- Implement tests
- Improve performance
- Implement CI/CD.