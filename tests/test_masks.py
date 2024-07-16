from pytest import mark, raises

from src.masks import get_mask_account, get_mask_card_number


@mark.parametrize(
    "card_number_input, card_number_output",
    [("7000792289606361", "7000 79** **** 6361"), ("8888000011112222", "8888 00** **** 2222")],
)
def test_get_mask_card_number_normal(card_number_input, card_number_output):
    assert get_mask_card_number(card_number_input) == card_number_output


def test_get_mask_card_number():
    with raises(ValueError) as exception_info:
        get_mask_card_number("7000 7922 8960 6361")
    assert str(exception_info.value) == "Некорректный номер карты. Должен быть строкой из 16 цифр."

    with raises(ValueError) as exception_info:
        get_mask_card_number("")
    assert str(exception_info.value) == "Некорректный номер карты. Должен быть строкой из 16 цифр."

    with raises(TypeError) as exception_info:
        get_mask_card_number(40)
    assert str(exception_info.value) == "Номер карты должен быть строкой."


@mark.parametrize(
    "account_number_input, account_number_output",
    [("73654108430135874305", "**4305"), ("73654108430135879999", "**9999")],
)
def test_get_mask_account_normal(account_number_input, account_number_output):
    assert get_mask_account(account_number_input) == account_number_output


def test_get_mask_account():
    with raises(ValueError) as exception_info:
        get_mask_account("asbb ")
    assert str(exception_info.value) == "Некорректный номер счёта. Должен быть строкой из 20 цифр."

    with raises(ValueError) as exception_info:
        get_mask_account("")
    assert str(exception_info.value) == "Некорректный номер счёта. Должен быть строкой из 20 цифр."

    with raises(TypeError) as exception_info:
        get_mask_account(40)
    assert str(exception_info.value) == "Номер счёта должен быть строкой."
