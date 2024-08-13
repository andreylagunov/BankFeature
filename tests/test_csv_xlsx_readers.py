from src.csv_xlsx_readers import get_transactions_dicts_from_csv, get_transactions_dicts_from_excel
from unittest.mock import Mock


def test_get_transactions_dicts_from_csv___not_exist():
    # Проверка возвращения пустого списка при передаче несуществующего пути
    assert get_transactions_dicts_from_csv("not_exist") == []

def test_get_transactions_dicts_from_csv___for_faulty():
    # Проверка возвращения пустого списка при некорректном содержимом csv
    assert get_transactions_dicts_from_csv("test_data/test_for_faulty.csv") == []

def test_get_transactions_dicts_from_csv___for_empty():
    # Проверка возвращения пустого списка при пустом файле
    assert get_transactions_dicts_from_csv("test_data/test_for_empty.csv") == []

def test_get_transactions_dicts_from_csv___for_normal():
    # Проверка нормальной работы
    list_of_dicts = get_transactions_dicts_from_csv("test_data/test_for_normal.csv")
    assert list_of_dicts[0]["description"] == "Перевод организации"
    assert list_of_dicts[1]["description"] == "Перевод с карты на карту"
    assert list_of_dicts[2]["description"] == "Перевод с карты на карту"
    assert list_of_dicts[3]["description"] == "Перевод с карты на карту"
    assert list_of_dicts[4]["description"] == "Открытие вклада"


def test_get_transactions_dicts_from_excel___not_exist():
    # Проверка возвращения пустого списка при передаче несуществующего пути
    assert get_transactions_dicts_from_excel("not_exist") == []

def test_get_transactions_dicts_from_excel___for_faulty():
    # Проверка возвращения пустого списка при некорректном содержимом csv
    assert get_transactions_dicts_from_excel("test_data/test_for_faulty.xlsx") == []

def test_get_transactions_dicts_from_excel___for_empty():
    # Проверка возвращения пустого списка при пустом файле
    assert get_transactions_dicts_from_excel("test_data/test_for_empty.xlsx") == []

def test_get_transactions_dicts_from_excel___for_normal():
    # Проверка нормальной работы
    list_of_dicts = get_transactions_dicts_from_excel("data/transactions_excel.xlsx")
    assert list_of_dicts[0]["description"] == "Перевод организации"
    assert list_of_dicts[1]["description"] == "Перевод с карты на карту"
    assert list_of_dicts[2]["description"] == "Перевод с карты на карту"
    assert list_of_dicts[3]["description"] == "Перевод с карты на карту"
    assert list_of_dicts[4]["description"] == "Открытие вклада"
