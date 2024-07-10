from src.widget import get_date


def filter_by_state(initial_lst: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей
    Возвращает список словарей, фильтрованный по state
    """
    return [dict_ for dict_ in initial_lst if dict_["state"] == state]


# list_to_filtering = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# print(filter_by_state(list_to_filtering))
# print(filter_by_state(list_to_filtering, state="CANCELED"))


def sort_by_date(initial_lst: list[dict], is_sorting_down: bool = True) -> list[dict]:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате (по умолчанию — убывание).
    """

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
