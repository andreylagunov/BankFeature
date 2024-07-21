from pytest import raises

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_normal(get_transactions_list):
    gen_func = filter_by_currency(get_transactions_list, "USD")
    assert next(gen_func) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen_func) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(gen_func) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

    gen_func = filter_by_currency(get_transactions_list, "RUB")
    assert next(gen_func) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(gen_func) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency():
    with raises(TypeError) as exception_info:
        # Передача не списка
        gen = filter_by_currency("4", "RUB")
        next(gen)
    assert str(exception_info.value) == "В функцию-генератор передан не спиcок."

    with raises(TypeError) as exception_info:
        # Передача currency-аргумента не строкового типа
        gen = filter_by_currency([1, 2], 2)
        next(gen)
    assert str(exception_info.value) == "Аргумент currency не str-типа."

    with raises(ValueError) as exception_info:
        # Передача пустого списка
        gen = filter_by_currency([], "USD")
        next(gen)
    assert str(exception_info.value) == "Список транзакций пуст."


def test_filter_by_currency_with_faulty_list(get_faulty_transactions_list):
    with raises(TypeError) as exception_info:
        # Передача пустого списка
        gen = filter_by_currency(get_faulty_transactions_list, "USD")
        assert type(next(gen)) is dict
        assert type(next(gen)) is dict
        next(gen)
    assert str(exception_info.value) == "В списке транзакции обнаружен элемент - не словарь."


def test_transaction_descriptions_normal(get_transactions_list):
    gen = transaction_descriptions(get_transactions_list)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


def test_transaction_descriptions_exceptions(get_faulty_transactions_list):
    with raises(TypeError) as exception_info:
        # Передача не списка с транзакциями
        gen = transaction_descriptions("not list[dict]")
        next(gen)
    assert str(exception_info.value) == "В функцию-генератор передан не спиcок."

    with raises(ValueError) as exception_info:
        # Передача пустого списка
        gen = transaction_descriptions([])
        next(gen)
    assert str(exception_info.value) == "Список транзакций пуст."

    with raises(TypeError) as exception_info:
        # Передача пустого списка
        gen = transaction_descriptions(get_faulty_transactions_list)
        next(gen)
        next(gen)
        next(gen)
    assert str(exception_info.value) == "В списке транзакции обнаружен элемент - не словарь."


def test_card_number_generator_normal():
    gen = card_number_generator(1, 5)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    assert next(gen) == "0000 0000 0000 0004"
    assert next(gen) == "0000 0000 0000 0005"

    gen = card_number_generator(9999_9999_9999_9995, 9999_9999_9999_9999)
    assert next(gen) == "9999 9999 9999 9995"
    assert next(gen) == "9999 9999 9999 9996"
    assert next(gen) == "9999 9999 9999 9997"
    assert next(gen) == "9999 9999 9999 9998"
    assert next(gen) == "9999 9999 9999 9999"


def test_card_number_generator_exceptions():
    with raises(TypeError) as exception_info:
        # Передача строкового значения start
        gen = card_number_generator("1", 5)
        next(gen)
    assert str(exception_info.value) == "В генератор номеров передан не int-тип."

    with raises(ValueError) as exception_info:
        # Передача отрицательного значения stop
        gen = card_number_generator(10, -50)
        next(gen)
    assert str(exception_info.value) == "В генератор номеров передано отрицательное значение."

    with raises(ValueError) as exception_info:
        # Передача start-аргумента, большего, нежели stop
        gen = card_number_generator(10, 3)
        next(gen)
    assert str(exception_info.value) == "Диапазон номеров для генерации указан некорректно. start > stop!"

    with raises(ValueError) as exception_info:
        # Передача start-аргумента, меньшего, нежели нижний предел, равный 1.
        gen = card_number_generator(0, 3)
        next(gen)
    assert (
        str(exception_info.value)
        == """Переданный диапазон генерации номеров недопустим,
                            Допускается 1 - 9999999999999999
        """
    )
