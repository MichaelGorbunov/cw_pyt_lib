import logging
import math
import os
from datetime import datetime
from typing import Any, Union

import pandas as pd
import requests
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

dat_tim_obj=datetime.now()

def get_response(date_time_str: str) -> str:
    """Главная функция, которая передает указаннаю дату и возвращает привествие"""
    greeting = get_greeting(datetime.strptime(date_time_str, "%d-%m-%Y %H:%M:%S"))
    return greeting

get_response("25-06-2024 00:00:01")
print(get_response("25-06-2024 00:00:01"))