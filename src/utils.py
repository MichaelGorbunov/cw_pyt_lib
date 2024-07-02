import logging
import os
from datetime import datetime
from typing import Any, Dict

import pandas as pd
from dotenv import load_dotenv

from config import LOGS_DIR

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")

logger = logging.getLogger("utils")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.DEBUG)


def get_greeting(time: datetime) -> str:
    """Возвращает приветствие в зависимости от времени дня"""
    hour = time.hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_response(date_time_str: str) -> str:
    """Главная функция, которая передает указаннаю дату и возвращает привествие"""
    logger.info(date_time_str)
    greeting = get_greeting(datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S"))
    logger.info(greeting)
    return greeting


def select_data(transactions: pd.DataFrame, date: str) -> pd.DataFrame:
    """Функция отбирает датафрейм за месяц"""

    end_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    start_date = end_date
    start_date = start_date.replace(day=1, microsecond=0)
    logger.info(end_date)
    logger.info(start_date)

    filtered_df = transactions[
        (transactions["datetime_col"] >= start_date) & (transactions["datetime_col"] <= end_date)
    ]
    logger.debug(len(filtered_df))
    return filtered_df


def get_data_group_by_card(transactions: pd.DataFrame) -> list[Dict] | Any:
    """функция принимает датафрейм и группирует операции по картам"""
    pay_operation = transactions[(transactions["Номер карты"].notna()) & (transactions["Сумма операции"] < 0.0)]
    response = []

    logger.debug(len(pay_operation))

    pay_operation_group = pay_operation.groupby(["Номер карты"]).agg({"Сумма операции": "sum"})
    cards_pay_dict = pay_operation_group.to_dict("index")

    for card_number, card_info in cards_pay_dict.items():
        total_spent = abs(round(card_info.get("Сумма операции"), 2))
        cashback = round((total_spent / 100), 2)

        response.append(
            {
                "last_digits": card_number,
                "total_spent": total_spent,
                "cashback": cashback,
            }
        )
    logger.debug(response)

    return response
    # return df_list


def get_top_transact(transaction: pd.DataFrame) -> list[Dict]:
    result = []
    df = transaction.sort_values(["Сумма операции"], ascending=True)
    top_transactions = df[:5].to_dict("records")

    for top_transaction in top_transactions:
        result.append(
            {
                "date": str(top_transaction["Дата операции"])[:10],
                "amount": top_transaction["Сумма операции"],
                "category": top_transaction["Категория"],
                "description": top_transaction["Описание"],
            }
        )
    logger.debug(result)
    return result


# from config import TEST_DIR
#
# test_date1 = "31-12-2021 00:00:01"
# test_df = pd.read_excel(os.path.join(TEST_DIR, "test_df.xlsx"))
# test_df["datetime_col"] = pd.to_datetime(test_df["Дата операции"], dayfirst=True)
# get_top_transact(test_df)
