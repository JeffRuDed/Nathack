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


def id_insta(database_file, search_value):
    found = False
    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 0:
            id_insta = data[0]
            if search_value in id_insta:
                Login = data[1]
                Password = data[2]
                Password1 = data[3]
                print(f'''{COLOR_CODE["RED"]}
╔══════                                               ══════╗
║                                                           ║ 
                {COLOR_CODE["RED"]}[+]ID пользователя: {id_insta}
                [+]Логин: {Login}
                [+]Пароль: {Password}
                [+]Двухфакторная аутентификация: {Password1}
                {COLOR_CODE["GREEN"]}
║                                                           ║
╚══════                                               ══════╝
                      ''')
                time.sleep(4)
                found = True

    if not found:
        print("Ничего не найдено в базе данных.")
        time.sleep(4)
time.sleep(4)
a = input('')