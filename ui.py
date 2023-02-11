import db_service
import table_service

def addNewNote():
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

def viewAllNotes():
    print(table_service.getId_and_header_notes_list(db_service.getAllNotes()))