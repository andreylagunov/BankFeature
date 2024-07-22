from src.decorators import log


# Тестирование записи в файл при нормальном выполнении
def test_log___for_file_write():
    @log("logs/logging.txt")
    def func():
        return "string"

    returned = func()
    assert returned == "string"
    with open("logs/logging.txt", "r", encoding="utf-8") as file:
        assert file.read() == "func, string"


# Тестирование записи в файл при ошибочном выполнении
def test_log___for_file_write___faulty():
    @log("logs/logging.txt")
    def func():
        raise ValueError("Ошибка значения")

    returned = func()
    assert returned is None
    with open("logs/logging.txt", "r", encoding="utf-8") as file:
        assert file.read() == "func error: Ошибка значения, Inputs: args=(), kwargs={}"


# Тестирование записи в файл при ошибочном выполнении (с аргументами)
def test_log___for_file_write___faulty___with_args():
    @log("logs/logging.txt")
    def func(*args, **kwargs):
        raise ValueError("Ошибка значения")

    returned = func(9.9, "ABC", name="Tommy")
    assert returned is None
    with open("logs/logging.txt", "r", encoding="utf-8") as file:
        assert file.read() == "func error: Ошибка значения, Inputs: args=(9.9, 'ABC'), kwargs={'name': 'Tommy'}"


# Тестирование вывода в консоль при нормальном выполнении
def test_log___for_console_output(capsys):
    @log()
    def func():
        return "string"

    returned = func()
    assert returned == "string"
    captured = capsys.readouterr()
    assert captured.out == "func, string\n"


# Тестирование вывода в консоль при ошибочном выполнении
def test_log___for_console_output___faulty(capsys):
    @log()
    def func():
        raise ValueError("Ошибка значения")

    returned = func()
    assert returned is None
    captured = capsys.readouterr()
    assert captured.out == "func error: Ошибка значения, Inputs: args=(), kwargs={}\n"


# Тестирование вывода в консоль при ошибочном выполнении (с аргументами)
def test_log___for_console_output___faulty___with_args(capsys):
    @log()
    def func(*args, **kwargs):
        raise ValueError("Ошибка значения")

    returned = func("a", "b", "c", next="def")
    assert returned is None
    captured = capsys.readouterr()
    assert captured.out == "func error: Ошибка значения, Inputs: args=('a', 'b', 'c'), kwargs={'next': 'def'}\n"
