import ui
import db_service

def start():
    print("Добро пожаловать в программу Заметки!\n")

    while True:
        command = input("\nВведите номер комманды из следующего списка:\n " + 
        "Посмотреть список всех заметок - 1\n Добавить новую заметку - 2\n Найти заметку по id - 3\n Поиск заметок по дате - 4\n Редактировать" + 
        " по id - 5\n Удалить заметку по id - 6\n Выйти - 7\n")

        if command == "1":
            ui.viewAllNotes()
        elif command == "2":
            ui.addNewNote()
        elif command == "7":
            exit()