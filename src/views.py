from config import DATA_DIR
import logging
import os
from config import DATA_DIR, LOGS_DIR, ROOT_DIR, url, url_stocks
from src.utils import get_response
import json
from src.categ import get_transaction_from_csv_file

logger = logging.getLogger("views")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "views.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.INFO)


def main(date):
    logger.info("Присваиваем переменным полученные результаты из функций")
    greeting = get_response(date)
    # course = getting_data_currencies(url, data_json)
    # stock_prices = getting_data_stock_prices(url_stocks, data_json)
    transactions = get_transaction_from_csv_file("1mont.csv")
    top_transactions = [
        {
            "date": "22.11.2021",
            "amount": -126105.03,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
        {"date": "04.10.2021", "amount": -91500.0, "category": "Медицина", "description": "Mikrokhirurgya Glaza"},
        {
            "date": "22.10.2021",
            "amount": -63021.01,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
        {"date": "17.11.2021", "amount": -50000.0, "category": "Переводы", "description": "Пополнение вклада"},
        {
            "date": "22.12.2021",
            "amount": -28001.94,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
    ]
    course = [{"currency": "USD", "rate": "64.1824"}, {"currency": "EUR", "rate": "69.244"}]
    stock_prices = [
        {"stock": "AAPL", "price": 208.14},
        {"stock": "AMZN", "price": 185.57},
        {"stock": "GOOGL", "price": 179.22},
        {"stock": "MSFT", "price": 447.67},
        {"stock": "TSLA", "price": 182.58},
    ]

    logger.info("Полученные данные преобразовываем в заданный словарь")
    response = {
        "greeting": greeting,
        "cards": transactions,
        "top_transactions": top_transactions,
        "currency_rates": course,
        "stock_prices": stock_prices,
    }

    logger.info("Выводим результат")
    logger.info(json.dumps(response, ensure_ascii=False, indent=4))
    return json.dumps(response, ensure_ascii=False, indent=4)


main("25-06-2024 00:00:01")
