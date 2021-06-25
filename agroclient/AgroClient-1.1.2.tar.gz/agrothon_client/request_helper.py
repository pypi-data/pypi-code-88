"""
@File    :   request_helper.py
@Path    :   agrothon_client/
@Time    :   2021/05/28
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.7
@Contact :   ckvbalusu@gmail.com
@Desc    :   API Request helper Module for Agrothon
"""
import requests
import io
from typing import Optional
from agrothon_client import SERVER_API_KEY, HOST
import logging
session = requests.Session()

LOGGER = logging.getLogger(__name__)

def sensor_data_post(json: dict) -> bool:
    base_url = f"{HOST}field/sensor?api_key={SERVER_API_KEY}"
    LOGGER.info("Started posting")
    resp = session.post(base_url, json=json)
    if resp.status_code == 200:
        LOGGER.info(resp.json())
        return True
    else:
        LOGGER.info(resp.status_code)
        return False


def image_poster(image: io.BytesIO) -> bool:
    base_url = f"{HOST}intruder/detect?api_key={SERVER_API_KEY}"
    LOGGER.info("Started posting IMage")
    data = {"image": image}
    resp = session.post(base_url, files=data)
    if resp.status_code == 200:
        return True
    else:
        return False


def pump_status_check() -> Optional[bool]:
    base_url = f"{HOST}pump/?api_key={SERVER_API_KEY}"
    resp = session.get(base_url)
    try:
        if resp.status_code == 200:
            data = resp.json()
            if data["status"]:
                return data["status"]
            elif not data["status"]:
                return False
            else:
                return None
        else:
            return None
    except Exception as e:
        LOGGER.error(e)
        pass