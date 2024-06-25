from config import DATA_DIR
import os
import pandas as pd
from datetime import datetime, timedelta
from src.data_conn import get_transaction_from_xlsx_file
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
from config import DATA_DIR, LOGS_DIR, ROOT_DIR

logger = logging.getLogger("reports")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "reports.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.INFO)

def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: [str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)"""
    if date is None:
        # logger.info("Установка текущей даты, если не задана дата")
        date = "2021-12-31"
        # selected_date = datetime.today().strftime()
        date_obj = datetime.strptime(date,"%Y-%m-%d")
    else:
        # logger.info("Преобразование в datetime заданой даты")
        selected_date = pd.to_datetime(date, dayfirst=True)

    start_date = date_obj + relativedelta(months=-2)#начало позапрошлого месяца
    start_date = start_date.replace(day=1)


    filtered_transactions =transactions.loc[(transactions["Категория"] == category)
    & (transactions["date_colum"] > start_date)]

    print(round(abs(filtered_transactions["Сумма операции"].sum()),2))
    return filtered_transactions
my_df = get_transaction_from_xlsx_file(os.path.join(DATA_DIR, "operations.xls"))


# print(spending_by_category(my_df,"Каршеринг"))

def data_set_3mont(transactions: pd.DataFrame,
                         date: [str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)"""
    if date is None:
        # logger.info("Установка текущей даты, если не задана дата")
        date = "2021-12-31"
        # selected_date = datetime.today().strftime()
        date_obj = datetime.strptime(date,"%Y-%m-%d")
    else:
        # logger.info("Преобразование в datetime заданой даты")
        selected_date = pd.to_datetime(date, dayfirst=True)

    start_date = date_obj + relativedelta(months=-2)#начало позапрошлого месяца
    start_date = start_date.replace(day=1)
    filtered_transactions =transactions.loc[(transactions["date_colum"] > start_date)]
    return filtered_transactions
# print(data_set_3mont(my_df))
ds_2=data_set_3mont(my_df)
# ds_2["Сумма операции"].nlargest(n=5)
ds_2.sort_values("Сумма операции", ascending=False).head(5)
ds_2.sort_values("Сумма операции", axis=0, ascending=True, inplace=True, kind='quicksort', na_position='last', ignore_index=True, key=None)
ds_2[:5].to_csv('top5.csv', encoding='utf-8')#первые пять с заголовком


def getting_top_specified_period(data: pd.DataFrame) -> list[dict]:
    """Фукнция, котораая возвращает топ-5 транзакций по сумме платежа"""
    top_transactions = data.to_dict("records")
    result = []

    for top_transaction in top_transactions:
        logger.info(top_transaction)
        result.append(
            {
                "date": top_transaction["Дата операции"][:10],
                "amount": top_transaction["Сумма операции"],
                "category": top_transaction["Категория"],
                "description": top_transaction["Описание"],
            }
        )


    return result
print(getting_top_specified_period(ds_2[:5]))