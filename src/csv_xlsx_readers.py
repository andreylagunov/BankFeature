import csv
import os
from typing import Any, Dict, List

import pandas as pd


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


def get_transactions_dicts_from_excel(file_path: str) -> List[Dict[Any, Any]]:
    """
    Принимает путь к файлу Excel (.xlsx),
    Возвращает список словарей с транзакциями.
    """
    # Если файл не существует:
    if not os.path.exists(file_path):
        return []

    try:
        excel_data = pd.read_excel(file_path)

        list_ = []
        colums_names_list = excel_data.columns.tolist()
        for index, row in excel_data.iterrows():
            list_.append({col_name: row[i] for i, col_name in enumerate(colums_names_list)})
        return list_

    except Exception:
        return []


# lst = get_transactions_dicts_from_excel("../data/transactions_excel.xlsx")
# print(type(lst))
# print(type(lst[0]), type(lst[-1]))
# for i in range(5):
#     print(lst[i])
