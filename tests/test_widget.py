from src.widget import mask_account_card
from src.widget import get_date
from pytest import raises
from pytest import mark


@mark.parametrize("number_input, number_output", [
                  ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                  ("Maestro 1596 8378 6870 5199", "Maestro 1596 83** **** 5199"),
                  ("Счет 64686473678894779589", "Счет **9589"),
                  ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                  ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                  ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                  ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
])
def test_mask_account_card_normal(number_input, number_output):
    assert mask_account_card(number_input) == number_output


def test_mask_account_card():
    with raises(ValueError) as exception_info:
        # В номере карты присутствует символ f
        assert mask_account_card("Maestro 15968378687051f")
        assert exception_info.value == "Проблема с номером карты/счёта."

    with raises(ValueError) as exception_info:
        assert mask_account_card("Счет 3538303347444795560")
        assert exception_info.value == "Проблема с номером карты/счёта."

    with raises(ValueError) as exception_info:
        assert mask_account_card("Сч 3538303347444795560")
        assert exception_info.value == "Проблема в названии счёта или номера карты. Ожидаются:   Счёт, Visa..."

    with raises(ValueError) as exception_info:
        assert mask_account_card("3538303347444795560")
        assert exception_info.value == "Проблема в названии счёта или номера карты. Ожидаются:   Счёт, Visa..."

    with raises(ValueError) as exception_info:
        assert mask_account_card("Maetro 15968378687051")
        assert exception_info.value == "Проблема в названии счёта или номера карты. Ожидаются:   Счёт, Visa..."

    with raises(ValueError) as exception_info:
        assert mask_account_card("card 15968378687051")
        assert exception_info.value == "Проблема в названии счёта или номера карты. Ожидаются:   Счёт, Visa..."

    with raises(ValueError) as exception_info:
        assert mask_account_card("")
        assert exception_info.value == "Проблема в названии счёта или номера карты. Ожидаются:   Счёт, Visa..."

    with raises(TypeError) as exception_info:
        assert mask_account_card(5)
        assert exception_info.value == "Приняты данные не типа str. Ожидается строка вида: Visa Platinum 7000 7922 8960 6361"


@mark.parametrize("date_input, date_output", [
                  ("2024-03-11T02:26:18.671407", "11.03.2024"),
                  ("2025-03-11T02:26:18.671407", "11.03.2025"),
                  ("2024-04-11T02:26:18.671407", "11.04.2024"),
])
def test_get_date_normal(date_input, date_output):
    assert get_date(date_input) == date_output


def test_get_date():
    with raises(TypeError) as exception_info:
        assert get_date(5)
        assert exception_info.value == "Формат данных даты должен быть типа str."

    with raises(ValueError) as exception_info:
        assert get_date("")
        assert exception_info.value == "Некорректный формат даты/времени."

    with raises(ValueError) as exception_info:
        # Передаётся "сороковой" месяц
        assert get_date("2024-40-11T02:26:18.671407")
        assert exception_info.value == "Некорректный формат даты/времени."

    with raises(ValueError) as exception_info:
        # Передаётся "восьмидесятый" день
        assert get_date("2024-03-80T02:26:18.671407")
        assert exception_info.value == "Некорректный формат даты/времени."

    with raises(ValueError) as exception_info:
        # Передаётся "сотый" день
        assert get_date("2024-03-100T02:26:18.671407")
        assert exception_info.value == "Формат строки даты не соответствует шаблону dddd-dd-ddTdd:dd:dd.dddddd"
