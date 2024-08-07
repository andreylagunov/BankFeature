import json
import logging
import os
from typing import Any, Dict, List

if os.path.exists("logs/utils.log"):
    os.truncate("logs/utils.log", 0)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs/utils.log")
formatter = logging.Formatter("%(asctime)s   %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_transactions_from_json(json_file_path: str) -> List[Dict[Any, Any]]:
    """
    Принимает на вход путь до JSON,
    Возвращает список словарей с данными о финансовых транзакциях.
    Возвращает пустой список в случаях: файл пустой / содержит не список / не найден.
    """
    # Если файл не существует:
    if not os.path.exists(json_file_path):
        logger.warning("Файл по указанному пути не существует.")
        logger.debug("Возвращается пустой список.")
        return []

    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            transactions_list = json.load(file)
        logger.debug("json-файл открыт без ошибок.")

    except Exception as ex:
        # Информация:
        logger.error(f"При попытке открытия файла {json_file_path}, произошла ошибка {ex}")
        logger.debug("Возвращается пустой список.")
        return []

    # Проверка содержимого (список ли, не пуст ли):
    if type(transactions_list) is not list or len(transactions_list) == 0:
        logger.warning("Содержимое json-файла: ожидался непустой список.")
        logger.debug("Возвращается пустой список.")
        return []
    else:
        logger.debug("Содержимое json-файла - ОК. Возвращается функцией.")
        return transactions_list


# returned = get_transactions_from_json("../data/operations.json")
# print(type(returned))
# print(len(returned))
# counter = 0
# for trans in returned:
#     counter += 1
#     if "description" in trans:
#         print(trans["description"], f", counter = {counter}")
