from src.external_api import get_transaction_amount_in_rub
from unittest.mock import patch


@patch("requests.get")
def test___get_transaction_amount_in_rub___from_usd(mock_requests_get):
    mock_requests_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 92688.46},
        "info": {"timestamp": 1722527416, "rate": 85.496804},
        "date": "2024-08-01",
        "result": 7924567.097682,
    }
    trans_example = {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
            "amount": "92688.46",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
    }
    assert get_transaction_amount_in_rub(trans_example) == 7924567.097682


def test___get_transaction_amount_in_rub___from_rub():
    trans_example = {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
            "amount": "92688.46",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
    }
    assert get_transaction_amount_in_rub(trans_example) == 92688.46
