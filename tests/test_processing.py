from pytest import raises

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(get_check_list):
    assert filter_by_state(get_check_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(get_check_list, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    with raises(TypeError) as exception_info:
        # Передаём аргумент state, не равный типу str
        filter_by_state(get_check_list, 4)
    assert str(exception_info.value) == "Входные аргументы: не соответствующий тип одного или нескольких."

    with raises(TypeError) as exception_info:
        # Передаём список без словарей
        filter_by_state([3, 4])
    assert str(exception_info.value) == "Элемент списка не словарь."

    with raises(ValueError) as exception_info:
        # Передаём список без словарей (пустой список)
        filter_by_state([])
    assert str(exception_info.value) == "В функцию фильтрации передан пустой список."

    with raises(TypeError) as exception_info:
        # Передаём не список
        filter_by_state("not_list")
    assert str(exception_info.value) == "Входные аргументы: не соответствующий тип одного или нескольких."

    with raises(ValueError) as exception_info:
        # Передаём аргумент state, отличный от 'EXECUTED' / 'CANCELED'
        filter_by_state(get_check_list, state="3")
    assert str(exception_info.value) == "Аргумент 'state' должен быть значениями: 'EXECUTED' / 'CANCELED'."


def test_filter_by_state_without_key(get_fault_list):
    with raises(ValueError) as exception_info:
        # Передаём словари, в которых нет ключа "state"
        filter_by_state(get_fault_list)
    assert str(exception_info.value) == "В одном или нескольких словарях (списка) отсутствует ключ 'state'."


def test_sort_by_date(get_check_list):
    assert sort_by_date(get_check_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(get_check_list, is_sorting_down=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    with raises(ValueError) as exception_info:
        # Передаём список без словарей (пустой)
        sort_by_date([])
    assert str(exception_info.value) == "Список словарей под сортировку пуст."

    with raises(TypeError) as exception_info:
        # Передаём не список
        sort_by_date(9)
    assert str(exception_info.value) == "Один или несколько аргументов имеют несоответствующий тип."

    with raises(TypeError) as exception_info:
        # Передаём список без словарей
        sort_by_date([9, "22"])
    assert str(exception_info.value) == "Элемент списка - не словарь."

    with raises(TypeError) as exception_info:
        # Передаём аргумент порядка сортировки не типа bool
        sort_by_date(get_check_list, is_sorting_down=9)
    assert str(exception_info.value) == "Один или несколько аргументов имеют несоответствующий тип."


def test_sort_by_date_without_date(get_dicts_list_without_date):
    with raises(ValueError) as exception_info:
        # Передаём словари, в которых нет ключа "date"
        sort_by_date(get_dicts_list_without_date)
    assert str(exception_info.value) == "В одном или нескольких словарях нет ключа 'date'."


def test_sort_by_date_with_faulty_date(get_dicts_list_with_faulty_date):
    with raises(TypeError) as exception_info:
        # Передаём словари, в которых по ключу "date" не тип str
        sort_by_date(get_dicts_list_with_faulty_date)
    assert str(exception_info.value) == "Тип данных по ключу 'date' - не str."
