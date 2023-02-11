

def getId_and_header_notes_list(list):
    id_and_header_notes = ""
    for i in range(len(list)):
        id_and_header_notes += list[i][0] + "\t" + list[i][1]
        if (i == 0): id_and_header_notes += "\n------------------"
        id_and_header_notes +="\n"
    return id_and_header_notes