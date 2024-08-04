from src.utils import get_transactions_from_json


def test___get_transactions_from_json___not_exist():
    # Если файл не существует:
    assert get_transactions_from_json("Несуществующий.txt") == []


def test___get_transactions_from_json___normal():
    assert get_transactions_from_json("data/operations.json")[0]["id"] == 441945886
    assert get_transactions_from_json("data/operations.json")[0]["state"] == "EXECUTED"
    assert get_transactions_from_json("data/operations.json")[0]["date"] == "2019-08-26T10:50:58.294041"
    assert get_transactions_from_json("data/operations.json")[0]["description"] == "Перевод организации"

    assert get_transactions_from_json("data/operations.json")[-1]["id"] == 667307132
    assert get_transactions_from_json("data/operations.json")[-1]["state"] == "EXECUTED"
    assert get_transactions_from_json("data/operations.json")[-1]["date"] == "2019-07-13T18:51:29.313309"
    assert get_transactions_from_json("data/operations.json")[-1]["description"] == "Перевод с карты на счет"
