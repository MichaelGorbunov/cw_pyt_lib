# import json
import os

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
    print(response)
    print(response.json())

    # response_data = json.loads(response.text)
    response_data = response.json()
    return float(response_data["result"])
    # return response_data


print(currency_conversion("EUR", 1.0))