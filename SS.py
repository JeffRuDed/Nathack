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

banner = '''

➤Пробив социальных сетей

▌ 1 - Пробив Инстаграмма
▌ 2 - Пробив Телеграмма (скоро)
▌ 3 - Пробив Одноклассников (скоро)
▌ 4 - Поиск по номеру VK (скоро)
▌ 5 - Поиск по базам данных (скоро)

'''

print(banner)
time.sleep(2)
selector = input('Введите пункт ➤ ')

if selector == '1':
    from insta import id_insta
    database_file = 'instagram.txt'
    search_value = input(f'{COLOR_CODE["YELLOW"]}Введите ID (Instagramm) ➥ ')
    id_insta(database_file, search_value)