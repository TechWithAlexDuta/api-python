import json


def read_json(file_path: str):
    """
    read file
    """
    with open(file_path, "r") as json_file:
        content = json_file.read()
    return content


def deserialize_json(json_data: str):
    """
    Deserialize JSON formatted str to a Python object.
    """
    content = json.loads(json_data)
    return content


def serialize_json(data_obj: object):
    """
    Serialize obj to a JSON formatted str
    """
    content = json.dumps(data_obj)
    return content
