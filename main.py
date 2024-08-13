from src.csv_xlsx_readers import get_transactions_dicts_from_csv, get_transactions_dicts_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, transactions_filtered_by_description
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card


def main() -> None:
    greeting_string = """Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:"""
    selection_str = """1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n
Пользователь: """
    format_selection_dict = {
        1: "Для обработки выбран JSON-файл.",
        2: "Для обработки выбран CSV-файл.",
        3: "Для обработки выбран XLSX-файл.",
    }
    format_selection_and_files_paths_dict = {
        "Для обработки выбран JSON-файл.": "data/operations.json",
        "Для обработки выбран CSV-файл.": "data/transactions.csv",
        "Для обработки выбран XLSX-файл.": "data/transactions_excel.xlsx",
    }

    # ===========================================================================================================
    # ==================================-     ВЫБОР ФАЙЛА ПОЛЬЗОВАТЕЛЕМ   =======================================
    # ===========================================================================================================

    print(greeting_string)
    while True:
        user_input = input(selection_str)

        if user_input in ("1", "2", "3"):
            user_format_selection = format_selection_dict[int(user_input)]
            print("\n" + user_format_selection)
            break
        else:
            print("Недопустимый выбор. Выберите вариант: 1, или 2, или 3")

    # ===========================================================================================================
    # =========     ОТКРЫТИЕ ВЫБРАННОГО ФАЙЛА И ФИЛЬТРАЦИЯ ПО:   "EXECUTED", "CANCELED", "PENDING"   ============
    # ===========================================================================================================

    while True:
        user_input = input(
            """\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING.\n
Пользователь: """
        ).upper()

        if user_input in ("EXECUTED", "CANCELED", "PENDING"):
            file_path = format_selection_and_files_paths_dict[user_format_selection]
            temp_trans_list = None

            if ".json" in file_path:
                temp_trans_list = get_transactions_from_json(file_path)
            elif ".csv" in file_path:
                temp_trans_list = get_transactions_dicts_from_csv(file_path)
            elif ".xlsx" in file_path:
                temp_trans_list = get_transactions_dicts_from_excel(file_path)

            filt_list = filter_by_state(temp_trans_list, user_input)
            # тесты
            #             print(f"Операции отфильтрованы по статусу '{user_input}'.")
            #             for dict_ in filt_list:
            #                 print(dict_)
            break
        else:
            print(f"\nСтатус операции '{user_input}' недоступен.")

    # ===========================================================================================================
    # =======================     ФОРМИРОВАНИЕ ДОПОЛНИТЕЛЬНЫХ КРИТЕРИЕВ ФИЛЬТРАЦИИ      =========================
    # ===========================================================================================================

    questions = {
        "Отсортировать операции по дате?": None,
        "Отсортировать по возрастанию? (если нет - сортировка по убыванию)": None,
        "Выводить только рублёвые транзакции?": None,
        "Отфильтровать по определённому слову в описании?": None,
        "Слово-фильтр: ": None,
    }
    question_tail = " Да/Нет\n\nПользователь: "

    for question in questions.keys():
        while question != "Слово-фильтр: ":

            if question == "Отсортировать по возрастанию? (если нет - сортировка по убыванию)":
                if questions["Отсортировать операции по дате?"] == "нет":
                    break

            yes_no_answer = input(f"\n{question}{question_tail}").lower()
            if yes_no_answer in ("да", "нет"):
                questions[question] = yes_no_answer
                if question == "Отфильтровать по определённому слову в описании?" and yes_no_answer == "да":
                    questions["Слово-фильтр: "] = input("Слово-фильтр: ")
                break
            print("Некорректый выбор.")

    # тесты
    #     print(questions)

    # ===========================================================================================================
    # ======================     ФИЛЬТРАЦИЯ ПО ДАТЕ, РУБЛЕВЫМ ОПЕРАЦИЯМ, ПО ОПИСАНИЮ     ========================
    # ===========================================================================================================

    if questions["Отсортировать операции по дате?"] == "да" and len(filt_list):
        if questions["Отсортировать по возрастанию? (если нет - сортировка по убыванию)"] == "нет":
            filt_list = sort_by_date(filt_list)
        else:
            filt_list = sort_by_date(filt_list, is_sorting_down=False)

    # тесты
    # print("Отсортированы по дате.")
    # for dict_ in filt_list:
    #     print(dict_)

    if questions["Выводить только рублёвые транзакции?"] == "да" and len(filt_list):
        filt_list = list(filter_by_currency(filt_list, "RUB"))

    # тесты
    #         print("Отсортированы по рублевым операциям.")
    #         for dict_ in filt_list:
    #             print(dict_)

    if questions["Отфильтровать по определённому слову в описании?"] == "да" and len(filt_list):
        filt_list = transactions_filtered_by_description(filt_list, questions["Слово-фильтр: "])

    # тесты
    #         print("Отсортированы по фразе-фильтру.")
    #         for dict_ in filt_list:
    #             print(dict_)

    # ===========================================================================================================
    # ==========================     ВЫВОД ИТОГОВОГО СПИСКА ТРАНЗАКЦИЙ     ======================================
    # ===========================================================================================================
    if len(filt_list):
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len(filt_list)}")

        for trans in filt_list:
            print(f"\n{get_date(trans["date"])} {trans["description"]}")

            # if "from" in trans and "to" in trans:
            if "from" in trans and str(trans["from"]) != "nan" and len(trans["from"]):
                print(f"{mask_account_card(trans["from"])} -> {mask_account_card(trans["to"])}")
            # elif "to" in trans:
            else:
                print(mask_account_card(trans["to"]))

            if (
                user_format_selection == "Для обработки выбран CSV-файл."
                or user_format_selection == "Для обработки выбран XLSX-файл."
            ):
                print(f"Сумма: {int(float(trans["amount"]))} {trans["currency_code"]}")

            elif user_format_selection == "Для обработки выбран JSON-файл.":
                print(
                    f"Сумма: {int(float(trans["operationAmount"]["amount"]))} \
{trans["operationAmount"]["currency"]["code"]}"
                )
    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


main()
