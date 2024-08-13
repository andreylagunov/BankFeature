import logging
import re

from src.utils import get_transactions_from_json      # импорт для тестов
from src.widget import get_date
from collections import Counter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs/utils.log")
formatter = logging.Formatter("%(asctime)s   %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def filter_by_state(initial_lst: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей
    Возвращает список словарей, фильтрованный по state
    """
    if type(initial_lst) is not list or type(state) is not str:
        raise TypeError("Входные аргументы: не соответствующий тип одного или нескольких.")

    if len(initial_lst) < 1:
        raise ValueError("В функцию фильтрации передан пустой список.")

    for dict_ in initial_lst:
        if type(dict_) is not dict:
            raise TypeError("Элемент списка не словарь.")

        if len(dict_) == 0:
            dict_["state"] = None
            continue

        if "state" not in dict_:
            raise ValueError("В одном или нескольких словарях (списка) отсутствует ключ 'state'.")

    if state not in ("EXECUTED", "CANCELED", "PENDING"):
        raise ValueError("Аргумент 'state' должен быть значениями: 'EXECUTED' / 'CANCELED' / 'PENDING'.")

    return [dict_ for dict_ in initial_lst if dict_["state"] == state]


# list_to_filtering = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# print(filter_by_state(list_to_filtering))
# print(filter_by_state(list_to_filtering, state="CANCELED"))


def sort_by_date(initial_lst: list[dict], is_sorting_down: bool = True) -> list[dict] | list:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате (по умолчанию — убывание).
    """
    if type(initial_lst) is not list or type(is_sorting_down) is not bool:
        raise TypeError("Один или несколько аргументов имеют несоответствующий тип.")

    if len(initial_lst) < 1:
        raise ValueError("Список словарей под сортировку пуст.")

    for dict_ in initial_lst:
        if type(dict_) is not dict:
            raise TypeError("Элемент списка - не словарь.")
        if "date" not in dict_:
            raise ValueError("В одном или нескольких словарях нет ключа 'date'.")
        if type(dict_["date"]) is not str:
            raise TypeError("Тип данных по ключу 'date' - не str.")

    def get_float_date(string: str) -> float:
        """
        Используется для промежуточного представления даты.
        Принимает дату вида     2024-03-11T02:26:18.671407
        Возвращает float (лет)  2024.2533...
        """
        date_str = get_date(string)
        years = int(date_str[-4:])
        months = int(date_str[3:5])
        days = int(date_str[:2])
        return years + months / 12 + days / 365

    return sorted(initial_lst, key=lambda dict_: get_float_date(dict_["date"]), reverse=is_sorting_down)


# list_to_sort = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# print(sort_by_date(list_to_sort))
# print(sort_by_date(list_to_sort, is_sorting_down=False))


def transactions_filtered_by_description(initial_lst: list[dict], pattern_for_search: str) -> list[dict] | list[None]:
    """
    Принимает список словарей с операциями и строку поиска.
    Возвращает список словарей, в описании которых есть искомая строка.
    """
    if type(pattern_for_search) is not str or pattern_for_search == "":
        return []

    pattern_for_search = pattern_for_search.lower()

    if "счёт" in pattern_for_search:
        pattern_for_search = pattern_for_search.replace("счёт", "счет")

    filtered_transactions_list = []
    for dict_ in initial_lst:
        if type(dict_) is not dict:
            continue
        if "description" in dict_ and type(dict_["description"]) is str:
            # Приводим значение из словаря к нижнему регистру:
            low_str = dict_["description"].lower()
            if "счёт" in low_str:
                low_str = low_str.replace("счёт", "счет")

            # match_obj = re.search(pattern_for_search, dict_["description"], flags=re.IGNORECASE)
            match_obj = re.search(pattern_for_search, low_str, flags=re.IGNORECASE)
            if match_obj is not None:
                filtered_transactions_list.append(dict_)
    return filtered_transactions_list


# list_ = transactions_filtered_by_description(get_transactions_from_json("../data/operations.json"), "на СЧёт")
# print(list_)


def get_dict_with_counted_categories(initial_lst: list[dict], categories_list: list) -> dict:
    """
    Принимает список словарей с транзакциями.
    Возвращает словарь вида: {"название категории": "количество операций в ней"}
    """
    list_ = []
    for dict_ in initial_lst:
        if type(dict_) is dict and "description" in dict_ and dict_["description"] in categories_list:
            list_.append(dict_["description"])

    # lst = [dict_["description"] for dict_ in initial_lst if "description" in dict_ and dict_["description"] in categories_list]
    # counted_categories = Counter(lst)

    counted_categories = Counter(list_)
    return dict(counted_categories)


# categories = ["Перевод с карты на карту", "Перевод со счета на счет", "Перевод организации", "Перевод с карты на счет"]
# categories = ["Открытие вклада", "Перевод организации"]
# categories = []
# transactions = get_transactions_from_json("../data/operations.json")
# dict_ = get_dict_with_counted_categories(transactions, categories)
# dict_ = get_dict_with_counted_categories(transactions, [9, 4, "Открытие вклада"])
# dict_ = get_dict_with_counted_categories(transactions, [9, 4])
# dict_ = get_dict_with_counted_categories(transactions, [])
# print(dict_)
