from datetime import datetime, timedelta
# date = None
# if date is None:
#     # logger.info("Установка текущей даты, если не задана дата")
#     date = "2021-12-31"
#     # selected_date = datetime.today().strftime()
#     date_obj = datetime.strptime(date, "%Y-%m-%d")
# # else:
#     # logger.info("Преобразование в datetime заданой даты")
#     # selected_date = pd.to_datetime(date, dayfirst=True)
#
# # start_date = date_obj + relativedelta(months=-2)  # начало позапрошлого месяца
# start_date = start_date.replace(day=1)
dt_now = datetime.today()
old_month=dt_now.month - 2
dt_now = dt_now.replace(month=old_month,day=1)
print(dt_now)
date_time_str = "25-06-2024 00:00:01"
test1=datetime.strptime(date_time_str, "%d-%m-%Y %H:%M:%S")
test1 = test1.replace(day=1)
print(test1)
print(type(test1))