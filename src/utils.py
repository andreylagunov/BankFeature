import json
import os
from typing import Any, Dict, List


def get_transactions_from_json(json_file_path: str) -> List[Dict[Any, Any]]:
    """
    Принимает на вход путь до JSON,
    Возвращает список словарей с данными о финансовых транзакциях.
    Возвращает пустой список в случаях: файл пустой / содержит не список / не найден.
    """
    # Если файл не существует:
    if not os.path.exists(json_file_path):
        return []

    # Если файл существует, открываем:
    with open(json_file_path, "r", encoding="utf-8") as file:
        transactions_list = json.load(file)

    # Проверка содержимого (список ли, не пуст ли):
    if type(transactions_list) is not list or len(transactions_list) == 0:
        return []
    else:
        return transactions_list


# returned = get_transactions_from_json("../data/operations.json")
# print(type(returned))
# print(len(returned))
# counter = 0
# for trans in returned:
#     counter += 1
#     if "description" in trans:
#         print(trans["description"], f", counter = {counter}")
