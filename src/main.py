from src.data_conn import get_dataframe
from src.reports import spending_by_category
from src.services import get_transfer_people
from src.views import get_views_data


def main() -> None:
    """запуск скриптов для получения данных в интерактивном режиме"""
    while True:
        json_view = input("вывести данные для веб страницы(да/нет) : ").lower()
        if json_view == "да":
            date = input("Введите дату в формате YYYY-MM-DD HH:MM:SS: ")
            print(get_views_data(date))
            break
        else:
            break
    while True:
        json_view = input("вывести данные переводов физическим лицам(да/нет) : ").lower()
        if json_view == "да":
            data_frame = get_dataframe()
            print(get_transfer_people(data_frame))
            break
        else:
            break
    while True:
        json_view = input("вывести траты по категории (да/нет): ").lower()
        if json_view == "да":
            date = input("Введите дату в формате YYYY-MM-DD :")
            category = input("Введите категорию : ")
            data_frame = get_dataframe()
            category_data = spending_by_category(data_frame, category, date)
            print(category_data)
            break
        else:
            break


if __name__ == "__main__":
    main()
