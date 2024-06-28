import os

import pandas as pd
# import pytest

from config import TEST_DIR
from src.reports import spending_by_category

test_date1 = "2021-12-31"
test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)


def test_spending_by_category():
    """тест выборка по дате"""
    result = spending_by_category(test_df, "Ж/д билеты", test_date1)
    assert len(result) == 2
