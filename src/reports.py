import logging
import os
from datetime import datetime, timedelta
from typing import Any

import pandas as pd

from config import DATA_DIR, LOGS_DIR

logger = logging.getLogger("reports")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "reports.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.DEBUG)


def write_to_file_params(file_name: str) -> Any:
    def decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            with open(os.path.join(DATA_DIR, file_name), "w", encoding="UTF-8") as file:
                file.write(result.to_string() + "\n")
            return result

        return wrapper

    return decorator


def file_save_decorators(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        result.to_csv(os.path.join(DATA_DIR, "cat_from_3m.csv"), encoding="utf-8")
        return result

    return wrapper


@write_to_file_params(file_name="function_report.txt")
@file_save_decorators
def spending_by_category(transactions: pd.DataFrame, category: str, date: str = "") -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)"""

    # cat_list: list = []
    if date == "":
        end_date = datetime.today()
        end_date = end_date.replace(microsecond=0)
        # end_day = end_date.day
        start_date = end_date - timedelta(days=90)
        # start_date = start_date.replace(day=end_day)
        logger.info(end_date)
        logger.info(start_date)
    else:

        end_date = datetime.strptime(date, "%Y-%m-%d")
        # end_day = end_date.day
        start_date = end_date - timedelta(days=90)
        # start_date = start_date.replace(day=end_day, microsecond=0)
        logger.info(end_date)
        logger.info(start_date)

    filtered_df = transactions[
        (transactions["datetime_col"] >= start_date) & (transactions["datetime_col"] <= end_date)
    ]
    cat_list = filtered_df["Категория"].unique()
    logger.debug(cat_list)
    if category in cat_list:
        result_df = filtered_df[(filtered_df["Категория"] == category)]
    else:
        result_df = pd.DataFrame()
    logger.info(len(result_df))
    logger.debug(result_df)
    # logger.debug(result_df.to_dict('index'))
    # result_df.to_csv(os.path.join(DATA_DIR, "cat_from_3m.csv"), encoding='utf-8')
    return result_df
