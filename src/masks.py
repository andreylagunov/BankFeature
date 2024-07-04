def get_mask_card_number(number: str) -> str:
    """
    Принимает: 7000792289606361
    Возвращает: 7000 79** **** 6361
    """
    return number[0:4] + " " + number[4:6] + "** **** " + number[-4:]


def get_mask_account(account: str) -> str:
    """
    Принимает: 73654108430135874305
    Возвращает **4305
    """
    return "**" + account[-4:]
