from datetime import datetime

FILE = "notes_db.csv"

def get_all_notes():
    temp_data = list()
    notes = list()

    with open(FILE, 'r', encoding='utf-8') as data:
        for line in data: temp_data.append(line)

    for i in temp_data:
        temp_list = i.split(';')
        temp_list[-1] = temp_list[-1][:-1:] # удаляет /n в конце последнего элемента списка, вообще любой элемент))) держи в базе переход на новую строку
        notes.append(temp_list)

    return notes

def add_new_note(note):
    id =get_new_id()
    write_data([id, note[0], note[1], datetime.now()])
    return id

def find_by_date_period(dates):
    all_notes = get_all_notes()
    result_notes = list()
    for i in range(len(all_notes)):
        if (i != 0):
            notes_date = datetime.strptime(all_notes[i][3].split(" ")[0], '%Y-%m-%d')
            if notes_date >= dates[0] and notes_date <= dates[1]:
                result_notes.append(all_notes[i])
        else: result_notes.append(all_notes[i])
    return result_notes

def find_by_id(id):
    all_notes = get_all_notes()
    for note in all_notes:
        if note[0] == id: return note

def get_new_id():
    all_notes = get_all_notes()
    id = 1
    if len(all_notes) != 0:
        last_id = all_notes[len(all_notes)-1][0]       
        if last_id.isdigit():
            id = int(last_id) + 1
    return id

def write_data(data):
    with open(FILE, 'a', encoding='utf-8') as file:
        file.write("\n")
        for i in range(len(data)):
            if i == len(data)-1:
                file.write(str(data[i]))
            else:
                file.write(str(data[i]))
                file.write(";")
        