import os

import pandas as pd
import pytest

# import json
from config import TEST_DIR
from src.services import get_transfer_people


# @pytest.fixture
def transactions_data_test():
    dict1 = [
        {
            "Дата операции": "30.08.2019 10:47:00",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма опереации": -100.0,
            "Категория": "Переводы",
            "MCC": 4814.0,
            "Описание": "Иван Ф.",
            "datetime_col": "30.08.2019 10:47:00",
        }
    ]
    return pd.DataFrame(dict1)


def test_get_transfer_people2():
    result = get_transfer_people(transactions_data_test())

    assert result == (
        '[\n    {\n        "Дата операции":"30.08.2019 10:47:00",\n        "Номер карты":"*4556",'
        '\n        "Статус":"OK",\n        "Сумма опереации":-100.0,\n        "Категория":"Переводы",'
        '\n        "MCC":4814.0,\n        "Описание":"Иван Ф.",'
        '\n        "datetime_col":"30.08.2019 10:47:00"\n    }\n]'
    )


# test_date1 = "2021-12-31"
# test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
# test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)
#
#
# def test_get_transfer_people():
#     result = get_transfer_people(test_df)
#
#     assert result != [
#         {
#             "Дата операции": 1640902923000,
#             "Дата платежа": 1640908800000,
#             "Номер карты": "*4556",
#             "Статус": "OK",
#             "Сумма операции": -20000.0,
#             "Валюта операции": "RUB",
#             "Категория": "Переводы",
#             "MCC": 7512.0,
#             "Описание": "Константин Л.",
#             "datetime_col": 1640902923000,
#         }
#     ]
