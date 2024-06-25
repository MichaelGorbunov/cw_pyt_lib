import pandas as pd
from typing import Any, Dict
def get_transaction_from_csv_file(path: str):
    """функция принимает путь до csv файла и возвращает список словарей"""
    blank_list: list = []
    transact_list = []
    try:
        df = pd.read_csv(path, delimiter=",", encoding="UTF-8")
        print(len(df))
        not_cancel_op = df.loc[df["MCC"].notna()]
        print(len(not_cancel_op))
        not_cancel_op1 = not_cancel_op.loc[not_cancel_op["Номер карты"] == "*7197" ]
        print(len(not_cancel_op1))
        print(not_cancel_op['Сумма операции'].sum())
        not_cancel_op2 = not_cancel_op.loc[not_cancel_op["Номер карты"] == "*5091"]
        print(len(not_cancel_op2))
        print(not_cancel_op2['Сумма операции'].sum())
        not_cancel_op3 = not_cancel_op.loc[not_cancel_op["Номер карты"] == "*4556"]
        print(len(not_cancel_op3))
        print(not_cancel_op3['Сумма операции'].sum())




        # return df_list
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        # return df_list

# get_transaction_from_csv_file("1mont.csv")
get_transaction_from_csv_file("1mont.csv")