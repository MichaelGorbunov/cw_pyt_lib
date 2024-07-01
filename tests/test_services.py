import pandas as pd

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
