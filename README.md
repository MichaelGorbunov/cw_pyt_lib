Проект 1. Приложение для анализа банковских операций. 

### Категория "веб-страницы"

В модуле views.py реализовано получение данных для страницы «Главная».

Функция, принимающую на вход строку с датой и временем в формате
YYYY-MM-DD HH:MM:SS и возвращающую JSON-ответ со следующими данными:

    Приветствие
    По каждой карте:
        последние 4 цифры карты;
        общая сумма расходов;
        кешбэк (1 рубль на каждые 100 рублей).
    Топ-5 транзакций по сумме платежа.
    Курс валют.
    Стоимость акций из S&P500.

### Категория "сервисы"

В модуле services.py реализован поиск  переводов физическим лицам.

Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физлицам.
Категория таких транзакций — "Переводы", а в описании есть имя и первая буква фамилии с точкой.

### Категория "отчеты". 

В модуле reports.py реализована функция возвращающая список транзакций по тратам в указанной категории.
Функция принимает на вход:

    датафрейм с транзакциями,
    название категории,
    опциональную дату.

Если дата не передана, то берется текущая дата.
Функция возвращает траты по заданной категории за последние три месяца (от переданной даты).
Создан декоратор для функций-отчетов
Декоратор без параметра — записывает данные отчета в файл **cat_from_3m.csv** в директории **data**.
Декоратор с параметром — принимает имя файла в качестве параметра.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/MichaelGorbunov/bank_app.git
```
2. Установите зависимости:
```
poetry install
```
## Работа модуля
Запуск программы:
```
python main.py
```
## Дополнительно:
Написаны тесты для реализованных функций. Степень покрытия тестами можно посмотреть:
```
 pytest --cov=src --cov-report term-missing
```

## Лицензия:

Этот проект можно использовать безвозмездно для любых, 
не противоречащих законодательству целей.