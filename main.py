from datetime import datetime
from dateutil.relativedelta import relativedelta

# Python теперь как машина времени
previous_month_date = datetime.now() + relativedelta(months=-2)
previous_month_date = previous_month_date.replace(day=1)
print(type(previous_month_date))
print(previous_month_date.strftime('%Y-%m-%d'))  # Провели успешное путешествие в прошлое!