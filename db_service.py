from datetime import datetime

FILE = "notes_db.csv"

def get_all_notes():
    temp_data = list()
    notes = list()

    try: 
        with open(FILE, 'r', encoding='utf-8') as data:
            for line in data: temp_data.append(line)

        for i in temp_data:
            temp_list = i.split(';')
            temp_list[-1] = temp_list[-1][:-1:] # удаляет /n в конце последнего элемента списка, вообще любой элемент))) держи в базе переход на новую строку
            notes.append(temp_list)
    except IOError:
        print("База данных пуста!")
    return notes

def add_new_note(note):
    id =get_new_id()
    data_list = list()
    data_list.append([id, note[0], note[1], datetime.now()])
    write_data(data_list, 'a')
    return id

def edit_note(edit_note):
    all_notes = get_all_notes()
    for i in range(len(all_notes)):
        if all_notes[i][0] == edit_note[0]:
            all_notes[i] = edit_note
    update_db(all_notes)
    return edit_note[0]

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

def update_db(notes):
    write_data(notes, 'w')

def write_data(list, mode):
    with open(FILE, mode, encoding='utf-8') as file:
        for data in list:
            if data[0] == 1:
                file.write("id;Заголовок;Текст_заметки;Дата_изменения")
            file.write("\n")
            for i in range(len(data)):
                if i == len(data)-1:
                    file.write(str(data[i]))
                else:
                    file.write(str(data[i]))
                    file.write(";")