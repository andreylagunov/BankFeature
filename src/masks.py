TYPE_ERROR_MESSAGE = "В функцию был передан тип, отличный от str и int"


def get_mask_card_number(card_number: str | int) -> str:
    """
    Функция принимает номер карты (строка или целое) вида 1111222233334444,
    возвращает строку вида 1111 22** **** 4444
    """
    if type(card_number) not in (str, int):
        raise TypeError(TYPE_ERROR_MESSAGE)

    if type(card_number) is not str:
        card_number = str(card_number)

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(card_number: str | int) -> str:
    """
    Функция принимает номер карты (строка или целое) вида 1111222233334444,
    возвращает строку вида **4444
    """
    if type(card_number) not in (str, int):
        raise TypeError(TYPE_ERROR_MESSAGE)

    if type(card_number) is not str:
        card_number = str(card_number)

    return f"**{card_number[-4:]}"
