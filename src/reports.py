from config import DATA_DIR
import os
import pandas as pd
from datetime import datetime, timedelta
from src.data_conn import get_transaction_from_xlsx_file
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

    # logger.info("Преобразование списка транзакций в DataFrame")
    # pd_transactions = pd.DataFrame(transactions)

    # logger.info("Находим отчетную дату за 3 месяца")
    three_months_ago_date_time = date_obj - timedelta(days=90)
    three_months_ago = three_months_ago_date_time.strftime("%Y.%m.%d")
    print(three_months_ago,three_months_ago_date_time)
    filtered_transactions =transactions.loc[(transactions["Категория"] == category)
    & (transactions["date_colum"] > three_months_ago_date_time)]

    print(round(abs(filtered_transactions["Сумма операции"].sum()),2))
    return filtered_transactions
my_df = get_transaction_from_xlsx_file(os.path.join(DATA_DIR, "operations.xls"))


print(spending_by_category(my_df,"Каршеринг"))