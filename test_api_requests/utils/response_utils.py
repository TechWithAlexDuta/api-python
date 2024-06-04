import json


def pretty_print(response):
    """
    Serialize obj to a JSON formatted str
    """
    json_obj = response.json()
    return json.dumps(json_obj, indent=4, sort_keys=True)