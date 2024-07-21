from typing import Any, Generator

# Пример данных для обработки:
# transactions = (
#     [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
# )


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict[Any, Any], None, None]:
    """
    Функция генератор.
    Принимает на вход список словарей, представляющих транзакции.
    Выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    if type(transactions_list) is not list:
        raise TypeError("В функцию-генератор передан не спиcок.")

    if type(currency) is not str:
        raise TypeError("Аргумент currency не str-типа.")

    if len(transactions_list) < 1:
        raise ValueError("Список транзакций пуст.")

    for trans in transactions_list:
        if type(trans) is not dict:
            raise TypeError("В списке транзакции обнаружен элемент - не словарь.")

        if trans["operationAmount"]["currency"]["code"] == currency:
            yield trans


# gen_func = filter_by_currency(transactions, "RUBL")
# for dict_ in gen_func:
#     print(dict_)


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str, None, None]:
    """
    Функция генератор.
    Принимает список словарей с транзакциями.
    Возвращает описание каждой операции по очереди.
    """
    if type(transactions_list) is not list:
        raise TypeError("В функцию-генератор передан не спиcок.")

    if len(transactions_list) < 1:
        raise ValueError("Список транзакций пуст.")

    for trans in transactions_list:
        if type(trans) is not dict:
            raise TypeError("В списке транзакции обнаружен элемент - не словарь.")

        yield trans["description"]


# descriptions_gen = transaction_descriptions(transactions)
# for description in descriptions_gen:
#     print(description)


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Принимает начальное и конечное значения для генерации диапазона номеров.
    Возвращает  0000 0000 0000 0001 мин.значение
                0000 0000 0000 0002
                0000 0000 0000 0003
                0000 0000 0000 0004
                0000 0000 0000 0005
                .... .... .... ....
                9999 9999 9999 9999 макс.значение
    """
    if type(start) is not int or type(stop) is not int:
        raise TypeError("В генератор номеров передан не int-тип.")

    if start < 0 or stop < 0:
        raise ValueError("В генератор номеров передано отрицательное значение.")

    if start > stop:
        raise ValueError("Диапазон номеров для генерации указан некорректно. start > stop!")

    if start < 1 or stop > 9999_9999_9999_9999:
        raise ValueError(
            """Переданный диапазон генерации номеров недопустим,
                            Допускается 1 - 9999999999999999
        """
        )

    for num in range(start, stop + 1):
        # из 1 получаем "0000000000000001"
        temp_str = str(num).rjust(16, "0")

        # Разбивка в "0000 0000 0000 0001"
        final_str = ""
        counter = 0
        for digit in temp_str:
            final_str += digit
            counter += 1
            if counter == 4 and len(final_str) != 19:
                final_str += " "
                counter = 0
        yield final_str


# card_num_gen = card_number_generator(9999_9999_9999_9995, 9999_9999_9999_9999)
# for number in card_num_gen:
#     if len(number) == 19:
#         print(number)
