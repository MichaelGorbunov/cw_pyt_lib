from config import DATA_DIR
import re
import pandas as pd
from src.data_conn import get_transaction_from_xlsx_file
import os
def get_transfer_people (transactions: pd.DataFrame):
    """Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физлицам."""
    f_dtf = transactions.loc[(transactions["Категория"] == "Переводы")]
    pattern = re.compile(r'[А-Я]{1}[а-я]{2,} [А-Я]{1}\.$')
    f_dtf = f_dtf[f_dtf["Описание"].str.contains(pattern)]
    # print(starting_with)
    return f_dtf



my_df = get_transaction_from_xlsx_file(os.path.join(DATA_DIR, "operations.xls"))
my_df2=get_transfer_people(my_df)
my_df2.to_csv('output.csv', encoding='utf-8')
