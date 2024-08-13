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


# list_ = get_transactions_dicts_from_csv("../data/transactions.csv")
# print(list_[0]["amount"])


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
#         =====================================================================
# тест
#         print(excel_data)

        # list_ = []
        lst = []
        # colums_names_list = excel_data.columns.tolist()
        # df_dict = excel_data.to_dict()
        # for dict_ in df_dict:
        #     print(dict_)
        # print(df_dict)

        # excel_row = excel_data.iloc[0]
            # print(colums_names_list)
            # print(excel_row)
            # print(type(excel_row))
        # dict_row = dict(excel_row)
            # print("dict_row: ", dict_row)
        # dict_row["id"] = str(dict_row["id"])
        # dict_row["amount"] = str(dict_row["amount"])
        # lst.append(dict_row)
            # print("dict_row: ", dict_row)
        # print("lst: ", lst)

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
        for index, row in excel_data.iterrows():
            dict_row = dict(row)
            dict_row["id"] = str(dict_row["id"])
            dict_row["amount"] = str(dict_row["amount"])
            lst.append(dict_row)
            # print(row)
            # FutureWarning: Series.__getitem__ treating keys as positions is deprecated.
            # In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior).
            # To access a value by position, use `ser.iloc[pos]`

            # list_.append({col_name: row[i] for i, col_name in enumerate(colums_names_list)})

        # for dict_ in lst:
        #     print(dict_)
        # return list_
        return lst
    except Exception:
        return []


lst = get_transactions_dicts_from_excel("../data/transactions_excel.xlsx")
# print(type(lst))
# print(type(lst[0]), type(lst[-1]))
# for i in range(5):
#     print(lst[i])
