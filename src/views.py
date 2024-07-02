import json
import logging
import os
from typing import Any

from config import LOGS_DIR, ROOT_DIR
from src.data_conn import get_dataframe
from src.external_api import getting_data_currencies, getting_data_stock_prices
from src.utils import get_data_group_by_card, get_response, get_top_transact, select_data

# from typing import Dict


logger = logging.getLogger("views")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "views.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.DEBUG)

with open(os.path.join(ROOT_DIR, "user_settings.json"), "r") as f:
    data_json = json.load(f)


def get_views_data(date_main: str) -> Any:
    """функция собирает данные из других источников и выводито json для веб-страницы"""
    logger.info("Присваиваем переменным полученные результаты из функций")
    data_frame = get_dataframe()
    greeting = get_response(date_main)
    date_select_df = select_data(data_frame, date_main)
    transactions_grp_card = get_data_group_by_card(date_select_df)
    top_transactions = get_top_transact(date_select_df)
    course = getting_data_currencies(data_json)
    stock_prices = getting_data_stock_prices(data_json)

    logger.info("Полученные данные преобразовываем в заданный словарь")
    response = {
        "greeting": greeting,
        "cards": transactions_grp_card,
        "top_transactions": top_transactions,
        "currency_rates": course,
        "stock_prices": stock_prices,
    }

    logger.info("Выводим результат")
    logger.debug(json.dumps(response, ensure_ascii=False, indent=4))
    return json.dumps(response, ensure_ascii=False, indent=4)
