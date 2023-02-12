import db_service
import table_service
from datetime import datetime

def add_new_Note():
    header = ""
    body = ""
    while True:
        header = input("Введите заголовок заметки:  ")
        if not header.strip(): 
            print("Заголовок не может быть пустым!")
            continue
        break
    while True:
        body = input("Введите текст заметки:  ")
        if not body.strip(): 
            print("Текст заметки не может быть пустым!")
            continue
        break
    print(f'Заметка успешно сохранена с id = {db_service.addNewNote([header, body])}') 

def search_notes_by_date():
    dates_str = input("Введите период дат для поиска (обе даты будут включены в поиск) через тире.\n" + 
    "Введите день, месяц и год через точку в формате 'дд.мм.гггг-дд.мм.гггг' (например: 01.03.2023-02.03.2023): ")
    try:
        start_date = datetime.strptime(dates_str.split("-")[0], '%d.%m.%Y')
        end_date = datetime.strptime(dates_str.split("-")[1], '%d.%m.%Y')
        print(table_service.print_notes_list(db_service.find_by_date_period([start_date, end_date])))
    except Exception:
        print("Вы ввели некорректные даты!")

def show_note():
    while True:
        id = input("Введите id заметки для отображения: ")
        if id.isdigit():
            print(table_service.print_note(db_service.find_by_id(id)))
            break
        else:
            print("Вы ввели не число!")


def view_all_notes():
    print(table_service.print_notes_list(db_service.get_all_notes()))