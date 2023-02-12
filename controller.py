import ui
import db_service

def start():
    print("Добро пожаловать в программу Заметки!\n")

    while True:
        command = input("\nВведите номер комманды из следующего списка:\n " + 
        "Посмотреть список всех заметок - 1\n Добавить новую заметку - 2\n " + 
        "Найти заметку по id - 3\n Поиск заметок по дате - 4\n Редактировать" + 
        " по id - 5\n Удалить заметку по id - 6\n Выйти - 7\n")

        if command == "1":
            ui.view_all_notes()
        elif command == "2":
            ui.add_new_note()
        elif command == "4":
            ui.search_notes_by_date()
        elif command == "7":
            exit()