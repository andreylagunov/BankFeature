def get_mask_card_number(number: str) -> str:
    """
    Принимает: 7000792289606361
    Возвращает: 7000 79** **** 6361
    """
    if type(number) is not str:
        raise TypeError("Номер карты должен быть строкой.")

    if len(number) != 16 or not number.isdigit():
        raise ValueError("Некорректный номер карты. Должен быть строкой из 16 цифр.")

    return number[0:4] + " " + number[4:6] + "** **** " + number[-4:]


def get_mask_account(account: str) -> str:
    """
    Принимает: 73654108430135874305
    Возвращает **4305
    """
    if type(account) is not str:
        raise TypeError("Номер счёта должен быть строкой.")

    if len(account) != 20 or not account.isdigit():
        raise ValueError("Некорректный номер счёта. Должен быть строкой из 20 цифр.")

    return "**" + account[-4:]
