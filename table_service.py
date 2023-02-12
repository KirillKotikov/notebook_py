

def print_note(note):
    note_str = "\nid: " + note[0]
    note_str += "\nДата изменения: " + note[3]
    note_str += "\nЗаголовок заметки: " + note[1]
    note_str += "\nТекст заметки:\n" + note[2]
    return note_str

def print_notes_list(list):
    id_and_header_notes = "\n"
    for i in range(len(list)):
        id_and_header_notes += list[i][0] + ";" + list[i][3] + ";" + list[i][1]
        if (i == 0): id_and_header_notes += "\n------------------------------------"
        id_and_header_notes +="\n"
    return id_and_header_notes