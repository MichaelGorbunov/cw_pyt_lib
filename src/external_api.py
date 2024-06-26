import json
import os

# import random
# from unittest.mock import mock_open, patch
from unittest.mock import patch
from config import DATA_DIR

# import pandas as pd
# import mock
import pytest


import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(currency: str, sum_transaction: float) -> float:
    # def currency_conversion(currency: str, sum_transaction: float, date_transact: str):
    """Конвертирует валюту через API и возвращает его в виде float"""

    # url = f"https://api.apilayer.com/exchangerates_data/
    # convert?to={'RUB'}&from={currency}&amount={sum_transaction}&date={date_transact}"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={sum_transaction}"
    # try:
    response = requests.get(url, headers={"apikey": API_KEY})
    # response.raise_for_status()
    # except requests.exceptions.RequestException:
    if response.status_code != 200:
        return 0.00

    # response_data = json.loads(response.text)
    response_data = response.json()
    return float(response_data["result"])


def my_function():
    with patch("requests.get") as mock_get:
        # Имитация обеспечивает мягкую работу теста
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "date": "2018-02-22",
            "historical": "",
            "info": {"rate": 148.972231, "timestamp": 1519328414},
            "query": {"amount": 1, "from": "EUR", "to": "RUB"},
            "result": 99,
            "success": True,
        }
        result = currency_conversion("EUR", 1.0)
        # assert result == 'test'
        return result


print(my_function())
