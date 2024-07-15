from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(initial_str: str) -> str:
    """
    Принимает:  Visa Platinum 7000 7922 8960 6361
    Возвращает: Visa Platinum 7000 79** **** 6361
        или
    Принимает:  Счет 73654108430135874305
    Возвращает: Счет **4305
    """
    if type(initial_str) is not str:
        raise TypeError("Приняты данные не типа str. Ожидается строка вида: Visa Platinum 7000 7922 8960 6361")

    prefix_str = ""  # Хранение "Visa Platinum " либо "Счёт "
    digits_str = ""  # Хранение "7000792289606361" либо "73654108430135874305"

    # Выборка строк "Visa Platinum " и "7000792289606361"
    is_prefix = True
    for symbol in initial_str:
        if is_prefix and symbol not in "0123456789":
            prefix_str += symbol
        else:
            is_prefix = False
            if symbol != " " and symbol in "0123456789":
                digits_str += symbol

    # Проверка на наличие в принимаемой строке названий "visa", "mastercard", "maestro", "счёт", "счет"
    is_prefix_valid = False
    valid_prefixes_of_accounts_and_cards = ("visa", "mastercard", "maestro", "счёт", "счет")
    for prefix in valid_prefixes_of_accounts_and_cards:
        if prefix in prefix_str.lower():
            is_prefix_valid = True
    if not is_prefix_valid:
        raise ValueError("Проблема в названии счёта или номера карты. Ожидаются:   Счёт, Visa...")

    if len(digits_str) == 16:
        return prefix_str + get_mask_card_number(digits_str)

    elif len(digits_str) == 20:
        return prefix_str + get_mask_account(digits_str)

    else:
        raise ValueError("Проблема с номером карты/счёта.")


def get_date(date_str: str) -> str:
    """
    Принимает: "2024-03-11T02:26:18.671407"
    Возвращает: "11.03.2024" (ДД.ММ.ГГГГ)
    """
    if type(date_str) is not str:
        raise TypeError("Формат данных даты должен быть типа str.")

    # Проверка шаблона принятой строки
    pattern_date_str = ""
    for symbol in date_str:
        if symbol.isdigit():
            pattern_date_str += "d"
        else:
            pattern_date_str += symbol
    if pattern_date_str != "dddd-dd-ddTdd:dd:dd.dddddd":
        raise ValueError("Формат строки даты не соответствует шаблону dddd-dd-ddTdd:dd:dd.dddddd")

    year_str = month_str = day_str = None

    if date_str[0:4].isdigit():
        year_str = date_str[0:4]

    if date_str[5:7].isdigit() and 1 <= int(date_str[5:7]) <= 12:
        month_str = date_str[5:7]

    if date_str[8:10].isdigit() and 1 <= int(date_str[8:10]) <= 31:
        day_str = date_str[8:10]

    if year_str and month_str and day_str:
        return f"{day_str}.{month_str}.{year_str}"
    else:
        raise ValueError("Некорректный формат даты/времени.")
