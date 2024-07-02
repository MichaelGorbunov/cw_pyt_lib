import os

import pandas as pd

from config import TEST_DIR
from src.utils import get_data_group_by_card, get_response, get_top_transact, select_data

# import pytest


test_date1 = "2021-12-31 00:00:01"
test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)


def test_get_response():
    """тест приветствия"""
    date = "2024-06-01 00:00:01"
    result = get_response(date)
    assert result == "Доброй ночи"


def test_select_data():
    """тест выборка по дате"""
    result = select_data(test_df, test_date1)
    assert len(result) == 5


def test_get_data_group_by_card():
    """группировка по картам"""
    result = get_data_group_by_card(test_df)
    assert result == [
        {"cashback": 214.11, "last_digits": "*4556", "total_spent": 21411.4},
        {"cashback": 0.07, "last_digits": "*5091", "total_spent": 7.07},
        {"cashback": 14.13, "last_digits": "*7197", "total_spent": 1412.72},
    ]


def test_get_top_transact():
    result = get_top_transact(test_df)
    assert result == [
        {"date": "2021-12-30", "amount": -20000.0, "category": "Переводы", "description": "Константин Л."},
        {"date": "2021-12-29", "amount": -1411.4, "category": "Ж/д билеты", "description": "РЖД"},
        {"date": "2021-12-29", "amount": -1411.4, "category": "Ж/д билеты", "description": "РЖД"},
        {"date": "2021-12-30", "amount": -7.07, "category": "Каршеринг", "description": "Ситидрайв"},
        {"date": "2021-12-30", "amount": -1.32, "category": "Каршеринг", "description": "Ситидрайв"},
    ]
