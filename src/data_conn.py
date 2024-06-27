import os

import pandas as pd

from config import DATA_DIR


def get_transaction_from_xlsx_file(path: str) -> pd.DataFrame:
    """функция извлекает транзакции из файла xlsx"""
    try:
        df = pd.read_excel(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")

    not_cancel_op = df.loc[df["Статус"] == "OK"]  # фильтруем некорретные опреации
    pd.options.mode.chained_assignment = None  # подавление ошибки SettingWithCopyWarning
    not_cancel_op["datetime_col"] = pd.to_datetime(not_cancel_op["Дата операции"], dayfirst=True)
    # делаем столбец в формате datatime b сортируем по нему
    not_cancel_op.sort_values(
        ["datetime_col"],
        axis=0,
        ascending=True,
        inplace=False,
        kind="quicksort",
        na_position="last",
        ignore_index=True,
        key=None,
    )
    return not_cancel_op


data_patch = os.path.join(DATA_DIR, "operations.xls")


def get_dataframe() -> pd.DataFrame:
    return get_transaction_from_xlsx_file(data_patch)
