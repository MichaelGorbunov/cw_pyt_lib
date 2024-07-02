import os

import pandas as pd

from config import TEST_DIR
from src.data_conn import get_transaction_from_xlsx_file

# import pytest


test_date1 = "2021-12-31"
test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
# test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)


def test_get_transaction_from_xlsx_file():
    result = get_transaction_from_xlsx_file(os.path.join(TEST_DIR, "test_df.xlsx"))
    assert len(result) == 5
