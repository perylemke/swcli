from httpx import get


def get_resources_dict(resource, label):
    resources_list = []
    for r in resource:
        resource_itens = get(r).json()[label]
        resources_list.append(resource_itens)
    return resources_list
