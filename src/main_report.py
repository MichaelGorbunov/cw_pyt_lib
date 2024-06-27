import pandas as pd

# Функция принимает на вход:
#     датафрейм с транзакциями,
#     название категории,
#     опциональную дату.
# Если дата не передана, то берется текущая дата.
# Функция возвращает траты по заданной категории за последние три месяца (от переданной даты).
from src.data_conn import get_dataframe
from src.reports import spending_by_category

df_empty = pd.DataFrame()
data_frame = get_dataframe()
df = spending_by_category(data_frame, "Косметика", "2021-12-31")
print(len(df))
