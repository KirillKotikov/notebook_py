from datetime import datetime

FILE = "notes_db.csv"

def getAllNotes():
    temp_data = list()
    notes = list()

    with open(FILE, 'r', encoding='utf-8') as data:
        for line in data: temp_data.append(line)

    for i in temp_data:
        temp_list = i.split(';')
        temp_list[-1] = temp_list[-1][:-1:] # удаляет /n в конце последнего элемента списка, вообще любой элемент))) держи в базе переход на новую строку
        notes.append(temp_list)

    return notes

def addNewNote(note):
    id =getNewId()
    writeData([id, note[0], note[1], datetime.now()])
    return id

def getNewId():
    allNotes = getAllNotes()
    id = 1
    if len(allNotes) != 0:
        last_id = allNotes[len(allNotes)-1][0]       
        if last_id.isdigit():
            id = int(last_id) + 1
    return id

def writeData(data):
    with open(FILE, 'a', encoding='utf-8') as file:
        file.write("\n")
        for i in range(len(data)):
            if i == len(data)-1:
                file.write(str(data[i]))
            else:
                file.write(str(data[i]))
                file.write(";")
        