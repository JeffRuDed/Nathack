import time

COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}


def get_id(database_file, search_value):
    found = False
    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 1:
            fio = data[0]
            if search_value in fio:
                fio = data[0]
                date_birth = data[1]
                sity = data[2]
                passport = data[3]
                gaved = data[4]
                mesto = data[5]
                cod = data[6]
                snils = data[7]
                inn = data[8]
                print(f'''{COLOR_CODE["RED"]}
                {fio}
                {date_birth}
                {sity}
                {passport}
                {gaved}
                {mesto}
                {cod}
                {snils}
                {inn}
                ''')

                time.sleep(4)
                found = True

    if not found:
        print("Ничего не найдено в базе")
        time.sleep(2)
