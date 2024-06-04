import logging
import pytest
import requests

import config.api_settings as api_settings
from utils.api_utils import post_products
from utils.json_utils import read_json
from utils.response_utils import pretty_print

LOGGER = logging.getLogger(__name__)

# run:  pytest -m api_tests --html=report.html


@pytest.mark.api_tests
def test_get_products():
    LOGGER.info("start API test")
    response = requests.get(
        f"{api_settings.base_url}{api_settings.get_products_endpoint}",
    )

    LOGGER.info(f"API response: \n {pretty_print(response)}")
    LOGGER.info(f"check status code is [200], actual value: {response.status_code}")
    assert response.status_code == 200

    LOGGER.info("end API test")


@pytest.mark.api_tests
def test_post_products():
    LOGGER.info("start API test")
    payload = read_json("data\\new_product.json")
    response = requests.post(
        f"{api_settings.base_url}{api_settings.post_products_endpoint}",
        headers={"Content-Type": "application/json"},
        data=payload,
    )

    LOGGER.info(f"API response: \n {pretty_print(response)}")

    LOGGER.info(f"check status code is [200], actual value: {response.status_code}")
    assert response.status_code == 200

    LOGGER.info("end API test")


@pytest.mark.api_tests
def test_get_product():
    id = post_products()
    LOGGER.info("start API test")
    response = requests.get(
        f"{api_settings.base_url}{api_settings.get_product_id_endpoint.format(id)}",
    )
    LOGGER.info(f"API response: \n {pretty_print(response)}")

    LOGGER.info(f"check status code is [200], actual value: {response.status_code}")
    assert response.status_code == 200

    LOGGER.info("end API test")


@pytest.mark.api_tests
def test_put_products():
    id = post_products()

    LOGGER.info("start API test")
    payload = read_json("data\\update_product.json")

    response = requests.put(
        f"{api_settings.base_url}{api_settings.put_products_endpoint.format(id)}",
        headers={"Content-Type": "application/json"},
        data=payload,
    )
    LOGGER.info(f"API response: \n {pretty_print(response)}")

    LOGGER.info(f"check status code is [200], actual value: {response.status_code}")
    assert response.status_code == 200

    LOGGER.info("end API test")


@pytest.mark.api_tests
def test_delete_products():
    id = post_products()
    LOGGER.info("start API test")
    response = requests.delete(
        f"{api_settings.base_url}{api_settings.delete_products_endpoint.format(id)}",
    )
    LOGGER.info(f"API response: \n {pretty_print(response)}")

    LOGGER.info(f"check status code is [200], actual value: {response.status_code}")
    assert response.status_code == 200

    LOGGER.info("end API test")
