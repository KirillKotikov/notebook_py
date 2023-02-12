import db_service
import table_service
from datetime import datetime

def add_new_note():
    print(f'Заметка успешно сохранена с id = {db_service.add_new_note(get_header_and_text_from_user())}')

def delete_by_id():
    id = get_id_from_user()
    if db_service.delete_note(id):
        print(f'Заметка с id = {id} успешно удалена!')
    else:     
        print(f'Заметка с id = {id} не найдена!')


def edit_note_by_id():
    edit_note = search_note_by_id()
    print("Заголовок заметки: " + edit_note[1] + "\n")
    print("Текст заметки: " + edit_note[2] + "\n")
    head_and_text = get_header_and_text_from_user()
    edit_note[1] = head_and_text[0]
    edit_note[2] = head_and_text[1]
    print(f'Заметка c id = {db_service.edit_note(edit_note)} изменена!')

def get_header_and_text_from_user():
    header = ""
    text = ""
    while True:
        header = input("Введите заголовок заметки:  ")
        if not header.strip(): 
            print("Заголовок не может быть пустым!")
            continue
        break
    while True:
        text = input("Введите текст заметки:  ")
        if not text.strip(): 
            print("Текст заметки не может быть пустым!")
            continue
        break
    return [header.replace(";", ""), text.replace(";", "")]

def get_id_from_user():
    while True:
        id = input("Введите id заметки: ")
        if id.isdigit():
            return id
        else:
            print("Вы ввели не число!")

def search_notes_by_date():
    dates_str = input("Введите период дат для поиска (обе даты будут включены в поиск) через тире.\n" + 
    "Введите день, месяц и год через точку в формате 'дд.мм.гггг-дд.мм.гггг' (например: 01.03.2023-02.03.2023): ")
    try:
        start_date = datetime.strptime(dates_str.split("-")[0], '%d.%m.%Y')
        end_date = datetime.strptime(dates_str.split("-")[1], '%d.%m.%Y')
        print(table_service.print_notes_list(db_service.find_by_date_period([start_date, end_date])))
    except Exception:
        print("Вы ввели некорректные даты!")

def search_note_by_id():
    return db_service.find_by_id(get_id_from_user())

def show_note_by_id():
    note = search_note_by_id()
    if note:
        print(table_service.print_note(note))
    else: print("Заметка с таким id не найдена!")

def view_all_notes():
    print(table_service.print_notes_list(db_service.get_all_notes()))