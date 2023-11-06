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
            get_id = data[1]
            if search_value in get_id:
                name = data[2]
                sex = data[3]
                inbaze = data[5]
                print(f'''{COLOR_CODE["RED"]}
╔══════                                               ══════╗
║                                                           ║ 
                {COLOR_CODE["RED"]}[+]ID пользователя: {get_id}
                [+]Имя: {name}
                [+]Пол: {sex}
                [+]В базе с: {inbaze}
                {COLOR_CODE["GREEN"]}
║                                                           ║
╚══════                                               ══════╝
                      ''')
                time.sleep(4)
                found = True

    if not found:
        print("Ничего не найдено в базе данных.")
        time.sleep(4)