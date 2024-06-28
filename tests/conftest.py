import pandas as pd
import pytest

from config import TEST_DIR


@pytest.fixture
def df_test():
    test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
    test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)
    return test_df


import pytest


@pytest.fixture
def transactions_data_test():
    return [
        {
            "Дата операции": "30.08.2019 10:47:00",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма опереации": -100.0,
            "Категория": "Переводы",
            "MCC": 4814.0,
            "Описание": "Иван Ф.",
            "datetime_col": "30.08.2019 10:47:00",
        },
    ]
