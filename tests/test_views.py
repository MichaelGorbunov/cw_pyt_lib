from src.views import main

test_date1 = "31-12-2021 00:00:01"


def test_main():
    result = main(test_date1)
    assert type(result) is str
