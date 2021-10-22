import settings
import utils
from httpx import get
from models import Vehicle


class GetVehicle(object):
    def get_vehicle_by_id(vehicle_id):
        """
        Return a one starship on Star Wars trilogies by ID.
        """
        response = get(
            settings.BASE_URL +
            settings.VEHICLES +
            str(vehicle_id))

        if response.status_code != 200:
            raise SystemExit('Resource does not exist!')

        json_data = response.json()

        vehicles_response = {
            "name": json_data['name'],
            "model": json_data['model'],
            "vehicle_class": json_data['vehicle_class'],
            "manufacturer": json_data['manufacturer'],
            "length": json_data['length'],
            "cost": json_data['cost_in_credits'],
            "crew": json_data['crew'],
            "passengers": json_data['passengers'],
            "max_atmosphering_speed": json_data['max_atmosphering_speed'],
            "cargo_capacity": json_data['cargo_capacity'],
            "consumables": json_data['consumables'],
            "films": utils.get_resources_dict(
                json_data['films'],
                'title'),
            "pilots": utils.get_resources_dict(
                json_data['pilots'],
                'name'),
        }

        vehicle = Vehicle(**vehicles_response)
        yield vehicle.json(ensure_ascii=False, encoder='utf-8')

    def get_vehicle_by_name(name):
        """
        Return a vehicle used on Star Wars universe.
        Like: TIE Fighter, Geonosian starfighter, etc.
        """
        json_data = get(
            settings.BASE_URL +
            settings.VEHICLES +
            settings.SEARCH +
            name).json()

        if not json_data['results']:
            raise SystemExit('Resource does not exist!')

        for json_dict in json_data['results']:

            vehicles_response = {
                "name": json_dict['name'],
                "model": json_dict['model'],
                "vehicle_class": json_dict['vehicle_class'],
                "manufacturer": json_dict['manufacturer'],
                "length": json_dict['length'],
                "cost": json_dict['cost_in_credits'],
                "crew": json_dict['crew'],
                "passengers": json_dict['passengers'],
                "max_atmosphering_speed": json_dict['max_atmosphering_speed'],
                "cargo_capacity": json_dict['cargo_capacity'],
                "consumables": json_dict['consumables'],
                "films": utils.get_resources_dict(
                    json_dict['films'],
                    'title'),
                "pilots": utils.get_resources_dict(
                    json_dict['pilots'],
                    'name'),
            }

            vehicle = Vehicle(**vehicles_response)
            yield vehicle.json(ensure_ascii=False, encoder='utf-8')
