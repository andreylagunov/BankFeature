import os

import requests
from dotenv import load_dotenv


def get_transaction_amount_in_rub(transaction_dict: dict) -> float:
    """
    Принимает на вход транзакцию (словарь),
    Возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR - конвертация через API.
    """
    if type(transaction_dict) is not dict or "operationAmount" not in transaction_dict:
        raise ValueError("Принятые данные отличаются от ожидаемого словаря-транзакции.")

    amount = transaction_dict["operationAmount"]["amount"]
    currency_code = transaction_dict["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return float(amount)
    else:
        load_dotenv()
        apilayer_token = os.getenv("APILAYER_TOKEN")

        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {"amount": amount, "from": currency_code, "to": "RUB"}

        headers = {"apikey": apilayer_token}

        response = requests.get(url, headers=headers, params=payload)
        # print("response.status_code: ", response.status_code)
        # print(response.json())
        response_dict = response.json()
        return response_dict["result"]


# trans_example = {
#     "id": 207126257,
#     "state": "EXECUTED",
#     "date": "2019-07-15T11:47:40.496961",
#     "operationAmount": {
#       "amount": "92688.46",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Открытие вклада",
#     "to": "Счет 35737585785074382265"
#   }
# amount = get_transaction_amount_in_rub(trans_example)
# print(amount)
