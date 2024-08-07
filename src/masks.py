import logging
import os

if os.path.exists("logs/masks.log"):
    os.truncate("logs/masks.log", 0)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs/masks.log")
formatter = logging.Formatter("%(asctime)s   %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_mask_card_number(number: str) -> str:
    """
    Принимает: 7000792289606361
    Возвращает: 7000 79** **** 6361
    """
    if type(number) is not str:
        logger.error("Номер карты: ожидался тип str.")
        raise TypeError("Номер карты должен быть строкой.")

    if len(number) != 16 or not number.isdigit():
        logger.error("Номер карты: ожидалась строка из 16 цифр.")
        raise ValueError("Некорректный номер карты. Должен быть строкой из 16 цифр.")

    result = number[0:4] + " " + number[4:6] + "** **** " + number[-4:]
    logger.info("Номер карты - ОК.")
    logger.debug(f"Возвращаемое значение: {result}")
    return result


def get_mask_account(account: str) -> str:
    """
    Принимает: 73654108430135874305
    Возвращает **4305
    """
    if type(account) is not str:
        logger.error("Номер счёта: ожидался тип str.")
        raise TypeError("Номер счёта должен быть строкой.")

    if len(account) != 20 or not account.isdigit():
        logger.error("Номер счёта: ожидалась строка из 20 цифр.")
        raise ValueError("Некорректный номер счёта. Должен быть строкой из 20 цифр.")

    result = "**" + account[-4:]
    logger.info("Номер счёта - ОК.")
    logger.debug(f"Возвращаемое значение: {result}")
    return result
