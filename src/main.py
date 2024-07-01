from src.data_conn import get_dataframe
from src.reports import spending_by_category
from src.services import get_transfer_people
from src.views import get_views_data
from datetime import datetime


def main() -> None:
    """запуск скриптов для получения данных в интерактивном режиме"""

    json_view = input("вывести данные для веб страницы(да/нет) : ").lower()
    if json_view == "да":
        date = input("Введите дату в формате YYYY-MM-DD HH:MM:SS: ")
        try:
            datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            print(get_views_data(date))
        except ValueError:
            print("ошибка ввода")

    json_view = input("вывести данные переводов физическим лицам(да/нет) : ").lower()
    if json_view == "да":
        data_frame = get_dataframe()
        print(get_transfer_people(data_frame))

    json_view = input("вывести траты по категории (да/нет): ").lower()
    if json_view == "да":
        date = input("Введите дату в формате YYYY-MM-DD :")
        category = input("Введите категорию : ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            data_frame = get_dataframe()
            category_data = spending_by_category(data_frame, category, date)
            print(category_data)
        except ValueError:
            print("ошибка ввода")


if __name__ == "__main__":
    main()
