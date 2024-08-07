import csv

# import pandas
import os
from typing import Any, Dict, List


def get_transactions_dicts_from_csv(file_path: str) -> List[Dict[Any, Any]]:
    """
    Принимает путь к файлу csv,
    Возвращает список словарей с транзакциями.
    """
    # Если файл не существует:
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, encoding="utf-8") as file:
            dict_reader = csv.DictReader(file, delimiter=";")
            return [dict(dict_) for dict_ in dict_reader]

    except Exception:
        return []


# get_transactions_dicts_from_csv("../data/transactions.csv")
