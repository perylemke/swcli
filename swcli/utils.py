from httpx import get


def query_by_id(resource_id, resource_type):
    """
    Realize a query on SW API and returns a list.
    """
    url = f'https://swapi.dev/api/{resource_type}/{resource_id}/'
    response = get(url)

    if response.status_code != 200:
        raise SystemExit('Resource does not exist!')

    # Include the return in a list
    json_data = []
    json_data.append(response.json())

    return json_data


def query_by_name(resource_name, resource_type):
    """
    Realize a query on SW API and returns a list.
    """
    url = f'https://swapi.dev/api/{resource_type}/?search={resource_name}'
    response = get(url).json()

    if not response['results']:
        raise SystemExit('Resource does not exist!')

    json_data = response['results']

    return json_data


def get_resources_dict(resource, label):
    resources_list = []
    for r in resource:
        resource_itens = get(r).json()[label]
        resources_list.append(resource_itens)
    return resources_list
