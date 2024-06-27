import json
import os

from config import ROOT_DIR
from src.data_conn import get_dataframe
from src.external_api import getting_data_currencies, getting_data_stock_prices
from src.utils import get_data_group_by_card, get_response, get_top_transact, select_data

# data_frame = get_dataframe()
# date_q = "31-12-2021 00:00:01"
# date_select_df = select_data(data_frame, date_q)
# get_response(date_q)
# get_data_group_by_card(date_select_df)
# get_top_transact(date_select_df)

with open(os.path.join(ROOT_DIR, "user_settings.json"), "r") as f:
    data_json = json.load(f)
getting_data_stock_prices(data_json)
# getting_data_currencies(data_json)
