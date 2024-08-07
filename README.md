# Виджет банковских операций клиента.


## Описание:

Учебный проект


## Необходимое ПО:

1. PyCharm IDE (или другая)
2. poetry
3. git
4. pytest
5. pytest-cov


## Для тестирования функций:

1. Клонируйте репозиторий:
```
git clone git@github.com:andreylagunov/BankFeature.git
```

2. Установите зависимости:

```
poetry install 
```

3. Для запуска тестирования инструментом pytest:

```
pytest
```

4. Для формирования отчёта о покрытии тестами инструментом pytest-cov:

```
pytest --cov=src --cov-report=html
```


## Описание работы функций:

### Модуль **masks.py**

```
get_mask_card_number()
     """
     Принимает: "7000792289606361"
     Возвращает: "7000 79** **** 6361"
     """

get_mask_account()
     """
     Принимает: "73654108430135874305"
     Возвращает "**4305"
     """

В рамках данного модуля при помощи функционала библиотеки logging 
происходит логгирование функций в файл masks.log
При каждом запуске приложения происходит перезапись лог-файла.
Методы логгирования и сообщения:
    error("Номер карты: ожидался тип str.")
    error("Номер карты: ожидалась строка из 16 цифр.")
    info("Номер карты - ОК.")
    debug(f"Возвращаемое значение: {result}")
    
    error("Номер счёта: ожидался тип str.")
    error("Номер счёта: ожидалась строка из 20 цифр.")
    info("Номер счёта - ОК.")
    debug(f"Возвращаемое значение: {result}")
```

### Модуль **widget.py**

```
mask_account_card()
    """
    Принимает:  Visa Platinum 7000 7922 8960 6361
    Возвращает: Visa Platinum 7000 79** **** 6361
          или
    Принимает:  Счет 73654108430135874305
    Возвращает: Счет **4305
    """
   
get_date()
    """
    Принимает: "2024-03-11T02:26:18.671407"
    Возвращает: "11.03.2024" (ДД.ММ.ГГГГ)
    """  
```

### Модуль **processing.py**

```
filter_by_state()
    """
    Принимает список словарей
    Возвращает список словарей, фильтрованный по state
    """

sort_by_date()
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате (по умолчанию — убывание).
    """
```

### Модуль **generators.py**
```
filter_by_currency()
    """
    Функция генератор.
    Принимает на вход список словарей, представляющих транзакции.
    Выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """

transaction_descriptions()
    """
    Функция генератор.
    Принимает список словарей с транзакциями.
    Возвращает описание каждой операции по очереди.
    """
    
card_number_generator()
    """
    Принимает начальное и конечное значения для генерации диапазона номеров.
    Возвращает  0000 0000 0000 0001 мин.значение
                0000 0000 0000 0002
                0000 0000 0000 0003
                0000 0000 0000 0004
                0000 0000 0000 0005
                .... .... .... ....
                9999 9999 9999 9999 макс.значение
    """
```

### Модуль **decorators.py**

```
@log()
# либо
@log(filename="filename.txt")
def function_name()

    """
    Логирование в указанный файл (filename) при его задании (иначе - вывод в консоль).
    Логирует:   - имя функции и результат выполнения                    - при успешной операции
                - имя функции, тип возникшей ошибки, входные параметры  - при возникновении ошибки
    """
```


### Модуль **utils.py**

```
get_transactions_from_json()
    """
    Принимает на вход путь до JSON,
    Возвращает список словарей с данными о финансовых транзакциях.
    Возвращает пустой список в случаях: файл пустой / содержит не список / не найден.
    """
    
В рамках данного модуля при помощи функционала библиотеки logging 
происходит логгирование функции в файл utils.log
При каждом запуске приложения происходит перезапись лог-файла.
Методы логгирования и сообщения:
    warning("Файл по указанному пути не существует.")
    debug("Возвращается пустой список.")
    debug("json-файл открыт без ошибок.")
    error(f"При попытке открытия файла {json_file_path}, произошла ошибка {ex}")
    warning("Содержимое json-файла: ожидался непустой список.")
    debug("Содержимое json-файла - ОК. Возвращается функцией.")
```


### Модуль **external_api.py**

```
get_transaction_amount_in_rub()
    """
    Принимает на вход транзакцию (словарь),
    Возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR - конвертация через API.
    """
```


### Модуль **csv_xlsx_readers.py**

```
get_transactions_dicts_from_csv()
    """
    Принимает путь к файлу csv,
    Возвращает список словарей с транзакциями.
    """
    
get_transactions_dicts_from_excel()
    """
    Принимает путь к файлу Excel (.xlsx),
    Возвращает список словарей с транзакциями.
    """
```


## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).