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


def get_card(database_file, search_value):
    found = False
    with open(database_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 2:
            get_card = data[3]
            if search_value in get_card:
                name = data[2]
                rod = data[1]
                data = data[4]
                number = data[5]
                adress = data[6]
                print(f'''{COLOR_CODE["RED"]}
                
                {COLOR_CODE["RED"]}[+]Номер карты: {card}
                [+]ФИО: {name}
                [+]Дата рождения: {rod}
                [+]Срок действия: {data}
                [+]Номер телефона: {number}
                [+]Адрес: {adress}
                {COLOR_CODE["GREEN"]}
                
                      ''')
                time.sleep(4)
                found = True
    if not found:
        print("Ничего не найдено в базе данных по номеру телефона.")
