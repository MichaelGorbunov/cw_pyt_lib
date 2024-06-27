import json
import logging
import os
import random
from typing import Any, Dict, Union

import requests
from dotenv import load_dotenv

from config import LOGS_DIR, ROOT_DIR, url, url_stocks

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")

logger = logging.getLogger("external_api")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "external_api.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.DEBUG)


def get_currency_fake(currency: str) -> float:
    result = round(random.uniform(85.7, 90.3), 2)
    logger.info(result)
    return result


def get_stock_fake(stock: str) -> float:
    result = round(random.uniform(185.7, 190.3), 2)
    logger.info(result)
    return result


# print(get_currency_fake("US"))
# print(get_stock_fake("APPL"))


def getting_data_currencies(currencies: dict) -> list[Dict] | Any:
    """Функция, которая получает данные о курсе валют из указанного API для заданной валюты"""
    result = []
    api = url
    try:
        logger.info("Перебираем валюты из заданного списка словарей валют")
        for currency in currencies["user_currencies"]:
            response = requests.get(api, params={"get": "rates", "pairs": f"{currency}RUB", "key": API_KEY})
            logger.debug(response.text)

            response_json = response.json()
            logger.info("Полученные данные преобразовываем в заданный словарь")
            result.append({"currency": currency, "rate": list(response_json["data"].values())[0]})
        logger.debug(result)
        return result
    except requests.exceptions.RequestException:
        logger.error("Запрос на сервис API не успешный")
        return []


with open(os.path.join(ROOT_DIR, "user_settings.json"), "r") as f:
    data_json = json.load(f)
    logger.info(data_json)


def getting_data_stock_prices(stocks: dict) -> Union[list[dict] | dict]:
    """Функция, которая получает данные о ценах акции из указанного API для заданной акции"""
    result = []
    api = url_stocks
    try:
        for stock in stocks["user_stocks"]:
            logger.info("Делаем запрос на сервис API для получения цен акций")
            response = requests.get(api, params={"symbol": stock, "token": API_KEY_STOCKS})

            logger.info("Получаем JSON данные")
            response_json = {"stock": stock, "data": response.json()}
            logger.info(response_json)

            logger.info("Полученные данные преобразовываем в заданный словарь")
            result.append({"stock": response_json["stock"], "price": response_json["data"]["c"]})

        logger.info("Выводим результат")
        logger.debug(result)
        return result
    except requests.exceptions.RequestException:
        logger.error("Запрос на сервис API не успешный")
        return []
