import time
from banner import bannerru
from pystyle import *
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
print(Colorate.Horizontal(Colors.cyan_to_blue,Center.XCenter(bannerru)))

select = input(f'{COLOR_CODE["RED"]}Введите пункт ➥ ')

if select == '1':
    from deanon_po_fio import get_fio
    database_file = 'QiWi.csv'
    search_value = input(f'{COLOR_CODE["YELLOW"]}Введите ФИО ')
    get_fio(database_file, search_value)
if select == '2':
    from deanon_po_id import get_id
    database_file = '18363883.csv'
    search_value = input(f'{COLOR_CODE["YELLOW"]}Введите ID ')
    get_id(database_file, search_value)
if select == '5':
    from ip import getIP
    getIP()
if select == '6':
    print("Подключенные библиотеки:")
    print("pystyle, os, json, urllib.request")
    time.sleep(4)
if select == '4':
    print("Базы данных находятся в исходной папке Nathack")
    time.sleep(4)
if select == '99':
    exit()
if select == '3':
    from DDos import dos
    dos()
if select == '7':
    from card import get_card
    database_file = 'card.xlsx'
    search_value = input(f'{COLOR_CODE["YELLOW"]}Введите номер карты: ')
    get_card(database_file, search_value)
if select == '8':
    import SS
    SS()