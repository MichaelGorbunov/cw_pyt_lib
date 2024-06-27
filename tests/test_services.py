import pytest
from src.services import get_transfer_people
import pandas as pd
import os
# import json
from config import TEST_DIR

test_date1 = "2021-12-31"
test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)


def test_get_transfer_people():
    result = (get_transfer_people(test_df))


    assert result != [
        {
            "Дата операции": 1640902923000,
            "Дата платежа": 1640908800000,
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": -20000.0,
            "Валюта операции": "RUB",
            "Категория": "Переводы",
            "MCC": 7512.0,
            "Описание": "Константин Л.",
            "datetime_col": 1640902923000
        }
    ]
