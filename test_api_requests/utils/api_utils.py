import logging

import requests

from utils.json_utils import deserialize_json, read_json
import config.api_settings as api_settings
from utils.response_utils import pretty_print


LOGGER = logging.getLogger(__name__)


def post_products():
    """
    create product helper function

    return obj['id']
    """
    LOGGER.info("start create product")
    payload = read_json("data\\new_product.json")
    response = requests.post(
        f"{api_settings.base_url}{api_settings.post_products_endpoint}",
        headers={"Content-Type": "application/json"},
        data=payload,
    )
    LOGGER.info(f"API response: \n {pretty_print(response)}")

    assert response.status_code == 200

    LOGGER.info("end create product")
    data_obj = deserialize_json(response.content)
    return data_obj["id"]
