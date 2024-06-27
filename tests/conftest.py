import pytest
import pandas as pd
from config import TEST_DIR

@pytest.fixture
def df_test():
    test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
    test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)
    return test_df
