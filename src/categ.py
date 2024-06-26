import pandas as pd
from typing import Any, Dict
def get_transaction_from_csv_file(path: str):
    """функция принимает путь до csv файла и возвращает список словарей"""
    blank_list: list = []
    transact_list = []
    try:
        df = pd.read_csv(path, delimiter=",", encoding="UTF-8")
        # print(len(df))
        not_cancel_op = df.loc[df["MCC"].notna()]
        response = []


        m = not_cancel_op.groupby(["Номер карты"]).agg({"Сумма операции": 'sum'})
        # m = not_cancel_op.groupby(["Номер карты"])
        cards_pay_dict = m.to_dict('index')
        # print(df_dict)
        # for q,w in df_dict.items():
        #     print(q,w.get("Сумма операции"))
        #     print()
        for card_number, card_info in cards_pay_dict.items():
            total_spent=abs(round(card_info.get("Сумма операции"), 2))
            cashback=round((total_spent/100),2)
            response.append(
                {
                    "last_digits": card_number,
                    "total_spent": total_spent,
                     "cashback": cashback,
                }
            )

        return response
        # return df_list
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        # return df_list

# get_transaction_from_csv_file("1mont.csv")
# get_transaction_from_csv_file("1mont.csv")