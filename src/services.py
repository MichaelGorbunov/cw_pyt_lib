import logging
import os
# import re
from typing import Any

import pandas as pd

from config import LOGS_DIR

logger = logging.getLogger("service")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "service.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.DEBUG)


def get_transfer_people(transactions: pd.DataFrame) -> Any:
    """Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физлицам."""
    logger.info("Получаем датафрейм")
    filtered_dtf = transactions[(transactions["Категория"] == "Переводы")]
    # pattern = re.compile(r"[А-Я]{1}[а-я]{2,} [А-Я]{1}\.$")
    # filtered_dtf = filtered_dtf[filtered_dtf["Описание"].str.contains(pattern)]
    filtered_dtf = filtered_dtf[filtered_dtf["Описание"].str.contains(r"[А-Я]{1}[а-я]{2,} [А-Я]{1}\.$", regex=True)]
    logger.debug(len(filtered_dtf))
    json_df = filtered_dtf.to_json(orient="records", indent=4, force_ascii=False)
    logger.debug(json_df)
    return json_df
