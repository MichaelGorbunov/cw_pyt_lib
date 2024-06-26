from config import DATA_DIR
import pandas as pd
from typing import Any, Dict
import os


def get_transaction_from_xlsx_file(path: str) -> pd.DataFrame:
    """функция извлекает транзакции из файла xlsx"""
    blank_list: list = []
    # transact_list = []
    try:
        df = pd.read_excel(path)
        not_cancel_op = df.loc[df["Статус"] == "OK"]
        pd.options.mode.chained_assignment = None  # подавление ошибки SettingWithCopyWarning
        not_cancel_op["date_colum"] = pd.to_datetime(not_cancel_op["Дата операции"], dayfirst=True)
        not_cancel_op.sort_values(
            ["Дата операции"],
            axis=0,
            ascending=True,
            inplace=False,
            kind="quicksort",
            na_position="last",
            ignore_index=True,
            key=None,
        )
        # print(not_cancel_op.info())

        return not_cancel_op
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        return blank_list


# print(len(get_transaction_from_xlsx_file(os.path.join(DATA_DIR, "operations.xls"))))
def get_category_list(pd):
    cat_list = []
    # print(excel_data["Категория"].unique())
    for items in pd["Категория"].unique():
        cat_list.append(items)
    print(cat_list)


def get_card_list(pd):
    card_list = []
    for items in pd["Номер карты"].unique():
        # print(type(items))
        if type(items) == float:  # фильтр NaN
            continue
        card_list.append(items)
    print(card_list)


# my_df = get_transaction_from_xlsx_file(os.path.join(DATA_DIR, "operations.xls"))
# get_category_list(my_df)
# get_card_list(my_df)
# print(len(my_df ))
# print(my_df)
