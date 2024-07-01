import json
import os
from unittest.mock import patch

import pandas as pd

import src.utils
import src.views
from config import TEST_DIR
from src.views import get_views_data

test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)
date = "2021-12-31 16:44:00"


# def test_response():
#     result = src.views.get_response(date)
#     assert result == "Добрый день"

def test_get_response():
    with patch("src.views.get_response") as call_fun_get_response:
        call_fun_get_response.return_value = "Ghbdtn"
        res = src.views.get_response("2021-12-31 00:44:00")
        assert res == "Ghbdtn"


@patch("src.views.getting_data_stock_prices")
@patch("src.views.getting_data_currencies")
@patch("src.views.get_top_transact")
@patch("src.views.get_data_group_by_card")
@patch("src.views.get_response")
def test_get_views_data(
    mock_response, mock_stosk_price, mock_data_currencies, mock_get_top_transact, mock_get_data_group_by_card
):
    mock_response.return_value = "sdfsdfs"
    mock_get_data_group_by_card.return_value = [
        {"last_digits": "*7197", "total_spent": -23562.64, "cashback": 0},
        {"last_digits": "*5091", "total_spent": -12742.92, "cashback": 0},
        {"last_digits": "*4556", "total_spent": 198770.3, "cashback": 181.0},
    ]
    mock_get_top_transact.return_value = [
        {"date": "2021-12-30", "amount": -20000.0, "category": "Переводы", "description": "Константин Л."},
        {"date": "2021-12-29", "amount": -1411.4, "category": "Ж/д билеты", "description": "РЖД"},
        {"date": "2021-12-29", "amount": -1411.4, "category": "Ж/д билеты", "description": "РЖД"},
        {"date": "2021-12-30", "amount": -7.07, "category": "Каршеринг", "description": "Ситидрайв"},
        {"date": "2021-12-30", "amount": -1.32, "category": "Каршеринг", "description": "Ситидрайв"},
    ]
    mock_data_currencies.return_value = [{"currency": "USD", "rate": "64.1824"}, {"currency": "EUR", "rate": "69.244"}]
    mock_stosk_price.return_value = [
        {"stock": "AAPL", "price": 207.49},
        {"stock": "AMZN", "price": 189.08},
        {"stock": "GOOGL", "price": 179.63},
        {"stock": "MSFT", "price": 449.78},
        {"stock": "TSLA", "price": 183.01},
    ]
    result = get_views_data(date)
    expected_result = {
        "cards": [
            {"price": 207.49, "stock": "AAPL"},
            {"price": 189.08, "stock": "AMZN"},
            {"price": 179.63, "stock": "GOOGL"},
            {"price": 449.78, "stock": "MSFT"},
            {"price": 183.01, "stock": "TSLA"},
        ],
        "currency_rates": [
            {"amount": -20000.0, "category": "Переводы", "date": "2021-12-30", "description": "Константин Л."},
            {"amount": -1411.4, "category": "Ж/д билеты", "date": "2021-12-29", "description": "РЖД"},
            {"amount": -1411.4, "category": "Ж/д билеты", "date": "2021-12-29", "description": "РЖД"},
            {"amount": -7.07, "category": "Каршеринг", "date": "2021-12-30", "description": "Ситидрайв"},
            {"amount": -1.32, "category": "Каршеринг", "date": "2021-12-30", "description": "Ситидрайв"},
        ],
        "greeting": "sdfsdfs",
        "stock_prices": [
            {"cashback": 0, "last_digits": "*7197", "total_spent": -23562.64},
            {"cashback": 0, "last_digits": "*5091", "total_spent": -12742.92},
            {"cashback": 181.0, "last_digits": "*4556", "total_spent": 198770.3},
        ],
        "top_transactions": [{"currency": "USD", "rate": "64.1824"}, {"currency": "EUR", "rate": "69.244"}],
    }
    assert json.loads(result) == expected_result
