# https://www.cbr-xml-daily.ru/daily_json.js
from config import DATA_DIR, LOGS_DIR, ROOT_DIR, url, url_stocks
import logging
import os
import json
import requests
from dotenv import load_dotenv
from src.data_conn import get_dataframe

load_dotenv()

fake_data_set = os.getenv("FAKE_DATA_SET")
fake_data_value = os.getenv("FAKE_DATA_VALUE")

logger = logging.getLogger("ext_api")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "ext_api.log"), encoding="utf8", mode="a")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.INFO)

# response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
# logger.info(response)
# response_json = response.text
# logger.info(response_json)
# # parsed_data - словарь, тип dict
# parsed_data = json.loads(response_json)
#
# # Получаем значение словаря по ключу
# print(parsed_data["Date"])

# import requests


def get_currency_rate():
    url = f"https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate ")
    data = json.loads(response.text)
    with open("currency.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# get_currency_rate()
if fake_data_set == "Yes":
    print(fake_data_value)
else:
    print("Текущая дата")

print(get_dataframe().info())