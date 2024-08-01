from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Логирование в указанный файл (filename) при его задании (иначе - вывод в консоль).
    Логирует:   - имя функции и результат выполнения                    - при успешной операции
                - имя функции, тип возникшей ошибки, входные параметры  - при возникновении ошибки
    """

    def wrapper(func: Callable) -> Callable:

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:

            try:
                returned = func(*args, **kwargs)
                normal_exec_str = f"{func.__name__}, {returned}"
                if filename is not None:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(normal_exec_str)
                else:
                    print(normal_exec_str)
                return returned

            except Exception as exception:
                faulty_exec_str = f"{func.__name__} error: {exception}, Inputs: args={args}, kwargs={kwargs}"
                if filename is not None:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(faulty_exec_str)
                else:
                    print(faulty_exec_str)
                return None

        return inner

    return wrapper
