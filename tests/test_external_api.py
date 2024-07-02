import json
import os
from unittest.mock import patch

from config import TEST_DIR
from src.external_api import getting_data_currencies, getting_data_stock_prices

with open(os.path.join(TEST_DIR, "user_settings_test.json"), "r") as f:
    data_json = json.load(f)


@patch("src.external_api.requests.get")
def test_getting_data_stock_prices_invalid(mocked_get):
    """ошибка запроса к API"""
    mocked_get.return_value.status_code = 400
    result = getting_data_currencies(data_json)
    assert result == []


@patch("src.external_api.requests.get")
def test_currency_conversion(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"data": {"USDRUB": "64.1824"}}
    result = getting_data_currencies(data_json)
    assert result == [{"currency": "USD", "rate": "64.1824"}]


@patch("src.external_api.requests.get")
def test_getting_data_stock_prices(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "stock": "AAPL",
        "data": {
            "c": 213.25,
            "d": 4.18,
            "dp": 1.9993,
            "h": 214.86,
            "l": 210.64,
            "o": 211.5,
            "pc": 209.07,
            "t": 1719360000,
        },
    }
    result = getting_data_stock_prices(data_json)
    assert result == [{"stock": "AAPL", "price": None}]
