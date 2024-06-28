import json
from unittest.mock import patch

# from src.config import date
from src.views import get_views_data

date = "2021-12-31 16:44:00"


@patch("src.views.data_json", return_value={})
def test_main(mock_data_json):
    # Mock the dependencies
    @patch("src.views.get_response")
    def mock_get_response(date, mock_get_response):
        return "Добрый день"

    @patch("src.views.transactions_grp_card")
    def mock_transactions_grp_card(mock_transactions_grp_card):
        return [
            {"last_digits": "*7197", "total_spent": -23562.64, "cashback": 0},
            {"last_digits": "*5091", "total_spent": -12742.92, "cashback": 0},
            {"last_digits": "*4556", "total_spent": 198770.3, "cashback": 181.0},
        ]

    @patch("src.views.get_top_transact")
    def mock_get_top_transact(transactions, mock_get_top_transact):
        return [
            {
                "date": "30.12.2021",
                "amount": 174000.0,
                "category": "Пополнения",
                "description": "Пополнение через Газпромбанк",
            },
            {
                "date": "22.12.2021",
                "amount": -28001.94,
                "category": "Переводы",
                "description": "Перевод Кредитная карта. ТП 10.2 RUR",
            },
            {
                "date": "22.12.2021",
                "amount": 28001.94,
                "category": "Переводы",
                "description": "Перевод Кредитная карта. ТП 10.2 RUR",
            },
            {"date": "23.12.2021", "amount": 20000.0, "category": "Другое", "description": "Иван С."},
            {"date": "30.12.2021", "amount": -20000.0, "category": "Переводы", "description": "Константин Л."},
        ]

    @patch("src.views.getting_data_currencies")
    def mock_getting_data_currencies(data_json, mock_getting_data_currencies):
        return [{"currency": "USD", "rate": "64.1824"}, {"currency": "EUR", "rate": "69.244"}]

    @patch("src.views.getting_data_stock_prices")
    def mock_getting_data_stock_prices(data_json, mock_getting_data_stock_prices):
        return [
            {"stock": "AAPL", "price": 207.49},
            {"stock": "AMZN", "price": 189.08},
            {"stock": "GOOGL", "price": 179.63},
            {"stock": "MSFT", "price": 449.78},
            {"stock": "TSLA", "price": 183.01},
        ]

    result = get_views_data(date)

    expected_result = {
        "greeting": "Добрый день",
        "cards": [
            {"last_digits": "*4556", "total_spent": 3775.7, "cashback": 37.76},
            {"last_digits": "*5091", "total_spent": 15193.33, "cashback": 151.93},
            {"last_digits": "*7197", "total_spent": 24278.63, "cashback": 242.79},
        ],
        "top_transactions": [
            {
                "date": "22.12.2021",
                "amount": -28001.94,
                "category": "Переводы",
                "description": "Перевод Кредитная карта. ТП 10.2 RUR",
            },
            {"date": "30.12.2021", "amount": -20000.0, "category": "Переводы", "description": "Константин Л."},
            {"date": "16.12.2021", "amount": -14216.42, "category": "ЖКХ", "description": "ЖКУ Квартира"},
            {"date": "23.12.2021", "amount": -10000.0, "category": "Переводы", "description": "Светлана Т."},
            {"date": "02.12.2021", "amount": -5510.8, "category": "Каршеринг", "description": "Ситидрайв"},
        ],
        "currency_rates": [{"currency": "USD", "rate": "64.1824"}, {"currency": "EUR", "rate": "69.244"}],
        "stock_prices": [
            {"stock": "AAPL", "price": 214.1},
            {"stock": "AMZN", "price": 197.85},
            {"stock": "GOOGL", "price": 185.41},
            {"stock": "MSFT", "price": 452.85},
            {"stock": "TSLA", "price": 197.42},
        ],
    }
    assert json.loads(result) == expected_result
