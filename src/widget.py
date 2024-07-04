from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(initial_str: str) -> str:
    """
    Принимает:  Visa Platinum 7000 7922 8960 6361
    Возвращает: Visa Platinum 7000 79** **** 6361
        или
    Принимает:  Счет 73654108430135874305
    Возвращает: Счет **4305
    """
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

    if len(digits_str) == 16:
        return prefix_str + get_mask_card_number(digits_str)

    elif len(digits_str) == 20:
        return prefix_str + get_mask_account(digits_str)

    else:
        raise ValueError("Проблема с номером карты/счёта")


assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
assert mask_account_card("Maestro 1596 8378 6870 5199") == "Maestro 1596 83** **** 5199"
assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
assert mask_account_card("Счет 35383033474447895560") == "Счет **5560"
assert mask_account_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
assert mask_account_card("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
assert mask_account_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
