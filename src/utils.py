import logging
import math
import os
import random
from datetime import datetime
from typing import Any, Union
from config import DATA_DIR, LOGS_DIR, ROOT_DIR, url, url_stocks
import pandas as pd
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")

logger = logging.getLogger("utils")

logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.INFO)


def get_greeting(time: datetime) -> str:
    """Возвращает приветствие в зависимости от времени дня"""
    hour = time.hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


dat_tim_obj = datetime.now()


def get_response(date_time_str: str) -> str:
    """Главная функция, которая передает указаннаю дату и возвращает привествие"""
    logger.info(date_time_str)
    greeting = get_greeting(datetime.strptime(date_time_str, "%d-%m-%Y %H:%M:%S"))
    logger.info(greeting)
    return greeting


# get_response("25-06-2024 00:00:01")
# print(get_response("25-06-2024 00:00:01"))


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


def getting_data_currencies(api: str, currencies: dict) -> list[dict]:
    """Функция, которая получает данные о курсе валют из указанного API для заданной валюты"""
    result = []
    try:
        logger.info("Перебираем валюты из заданного списка словарей валют")
        for currency in currencies["user_currencies"]:
            logger.info("Делаем запрос на сервис API для получения курса валют")
            logger.info(currency)

            response = requests.get(api, params={"get": "rates", "pairs": f"{currency}RUB", "key": API_KEY})
            logger.info({"get": "rates", "pairs": f"{currency}RUB", "key": API_KEY})

            logger.info("Получаем JSON данные")
            logger.info(response)

            response_json = response.json()

            logger.info("Полученные данные преобразовываем в заданный словарь")
            result.append({"currency": currency, "rate": list(response_json["data"].values())[0]})

        logger.info("Выводим результат")
        logger.info(result)
        return result
    except requests.exceptions.RequestException:
        logger.error("Запрос на сервис API не успешный")
        return []


with open(os.path.join(ROOT_DIR, "user_settings.json"), "r") as f:
    data_json = json.load(f)
    logger.info(data_json)

# getting_data_currencies("https://currate.ru/api/",data_json)
# getting_data_currencies(url, data_json)


def getting_data_stock_prices(api: str, stocks: dict) -> Union[list[dict] | dict]:
    """Функция, которая получает данные о ценах акции из указанного API для заданной акции"""
    result = []
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
        logger.info(result)
        return result
    except requests.exceptions.RequestException:
        logger.error("Запрос на сервис API не успешный")
        return []


# getting_data_stock_prices("https://finnhub.io/api/v1/quote",data_json)
# getting_data_stock_prices(url_stocks, data_json)
