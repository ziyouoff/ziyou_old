import os 
import sys
import pickle
import baners
import main
import webbrowser

try:
    from colorama import init, Fore
    from colorama import Back
    from colorama import Style
except:
    os.system('pip install colorama')
    from colorama import init, Fore
    from colorama import Back
    from colorama import Style

try:
    from pystyle import Center
except:
    os.system('pip install pystyle')
    from pystyle import Center

try:
    from termcolor import colored
except:
    os.system('pip install termcolor')
    from termcolor import colored

try:
    from rich import print
    from rich.layout import Layout
except:
    os.system('pip install rich')
    from rich import print
    from rich.layout import Layout

############################################################
############################################################
############################################################
def setings():
    global data

    with open('save', 'rb') as file:
        data = pickle.load(file)

    baners.print_ascll_setings()

    print(Center.XCenter(colored('╔═════════════════════════════════╗', "yellow")))
    print(Center.XCenter(colored('║1) Устройство                 [' + data['devise'] +']║', "yellow")))
    print(Center.XCenter(colored('║2) Вывод баз                  [' + data['base_out'] + ']║', "yellow")))
    print(Center.XCenter(colored('║3) Приветственная анимация    [' + data['hello_anim'] + ']║', "yellow")))
    print(Center.XCenter(colored('║                                 ║', "yellow")))
    print(Center.XCenter(colored('║b) Вернутся                      ║', "yellow")))
    print(Center.XCenter(colored('╚═════════════════════════════════╝', "yellow")))

    select_setings = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

    if select_setings == 'b':
        main_menu()

    elif select_setings == '1':
        print(Center.XCenter(colored('╔════════════════════════╗', "yellow")))
        print(Center.XCenter(colored('║ [P] - PC версия        ║', "yellow")))
        print(Center.XCenter(colored('║ [M] - Мобильная версия ║', "yellow")))
        print(Center.XCenter(colored('║                        ║', "yellow")))
        print(Center.XCenter(colored('║ [b] - Вернуься         ║', "yellow")))
        print(Center.XCenter(colored('╚════════════════════════╝', "yellow")))

        select_devise = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))
        data['devise'] = select_devise
        with open("save","wb") as save:
            pickle.dump(data,save)
        setings()

    elif select_setings == '2':
        print(Center.XCenter(colored('╔══════════════════════════╗', "yellow")))
        print(Center.XCenter(colored('║ [T] - Структура дерева   ║', "yellow")))
        print(Center.XCenter(colored('║ [S] - Стандартная версия ║', "yellow")))
        print(Center.XCenter(colored('║                          ║', "yellow")))
        print(Center.XCenter(colored('║ [b] - Вернуься           ║', "yellow")))
        print(Center.XCenter(colored('╚══════════════════════════╝', "yellow")))

        select_base_out = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))
        data['base_out'] = select_base_out
        with open("save","wb") as save:
            pickle.dump(data,save)
        setings()

    elif select_setings == '3':
        print(Center.XCenter(colored('╔══════════════════════════╗', "yellow")))
        print(Center.XCenter(colored('║ [1] - On                 ║', "yellow")))
        print(Center.XCenter(colored('║ [0] - Off                ║', "yellow")))
        print(Center.XCenter(colored('║                          ║', "yellow")))
        print(Center.XCenter(colored('║ [b] - Вернуься           ║', "yellow")))
        print(Center.XCenter(colored('╚══════════════════════════╝', "yellow")))

        select_status_start_anim = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))
        data['hello_anim'] = select_status_start_anim
        with open("save","wb") as save:
            pickle.dump(data,save)
        setings()


     

############################################################
############################################################
############################################################


def download_db(URL, NAME):
    import gdown
    osname = os.name
    output_file = os.path.dirname(os.path.abspath(__file__))
    if osname == 'nt': 
        output_file = output_file + "\src\\" + NAME
    elif osname == 'posix': 
        output_file = output_file + "/src/" + NAME

    YorN = input('Вы уверены что хотите установить базу {name}? [Y/n]: ')
    if YorN == 'n':
        main.main_menu()

    gdown.download(URL, output_file, quiet=False, fuzzy=True)
    
def del_db(NAME):
    osname = os.name
    if osname == 'nt': os.system('DEL src\\' + NAME)
    elif osname == 'posix': os.system('rm -rf src/' + NAME)


def uclear():
    osname = os.name
    if osname == 'nt': os.system('cls')
    elif osname == 'posix': os.system('clear')

############################################################
############################################################
############################################################

def start_serch_name():
    import serch_name
    fio = input(Center.XCenter(colored("[+]Введите имя: ", "cyan")))

    serch_name.pasports_1(fio)
    serch_name.tele2_1_06_22(fio)
    serch_name.zdravcity_1_01_23(fio)
    serch_name.gemotest(fio)
    serch_name.ru_base(fio)

##############################

def start_serch_phone():
    import serch_phone
    phone = input(Center.XCenter(colored("[+]Введите номер телефона для поиска(без +): ", "cyan")))
    
    serch_phone.tele2_1_06_22(phone)
    serch_phone.zdravcity_1_01_23(phone)
    serch_phone.DNSS_1_09_2022(phone)
    serch_phone.gemotest(phone)

##############################

def start_serch_telegram():
    import serch_telegram
    print(colored(baners.telegram_logo, "cyan"))
    uid = input(Center.XCenter(colored("[+]Введите user_name пользователя: ", "cyan")))

    serch_telegram.find_phone_by_uid_1(uid)
    serch_telegram.find_phone_by_uid_2(uid)
    serch_telegram.find_phone_by_uid_3(uid)
    

##############################

def start_serch():
    baners.print_start()
    print(Center.XCenter(colored('┌──────────────────────────────────┐', "yellow")))
    print(Center.XCenter(colored('├[1] - Поиск по номеру             │', "yellow")))
    print(Center.XCenter(colored('├[2] - Поиск по имени              │', "yellow")))
    print(Center.XCenter(colored('├[3] - Поиск по user_name telegram │', "yellow")))
    print(Center.XCenter(colored('│                                  │', "yellow")))
    print(Center.XCenter(colored('├[b] - Вернутся                    │', "yellow")))
    print(Center.XCenter(colored('└──────────────────────────────────┘', "yellow")))

    select_info_type = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))
    import serch_phone
    import serch_name
    import serch_telegram

    if select_info_type == '1': serch_phone.start_serch()
    elif select_info_type == '2': serch_name.start_serch()
    elif select_info_type == '3': serch_telegram.start_serch()

############################################################
############################################################
############################################################

def install():
    if os.path.exists("src/"):
        print(Center.XCenter(colored("[OK]src cоздан", "grey")))
    else:
        os.system('mkdir src')
            
    print(Center.XCenter(colored('┌────────────────────────────────────────────────────────────┐', "yellow")))
    print(Center.XCenter(colored('│                        Установщик                          │', "yellow")))
    print(Center.XCenter(colored('├────────────────────────────────────────────────────────────┤', "yellow")))
    print(Center.XCenter(colored('│       B1 - Установить       |         D1 - Удалить         │', "yellow")))
    print(Center.XCenter(colored('├────────────────────────────────────────────────────────────┤', "yellow")))
    print(Center.XCenter(colored('│ В случае ошибок, неработы баз или ошибки при установки     │', "yellow")))
    print(Center.XCenter(colored('│ проверте наличие папки src и ее содержимого                │', "yellow")))
    print(Center.XCenter(colored('│ вот решения возможных проблем                              │', "yellow")))
    print(Center.XCenter(colored('│ 1) Установите библиотеку GDown[L9]                         │', "yellow")))
    print(Center.XCenter(colored('│ 2) При отсутсвии папки src просто создайте ее              │', "yellow")))
    print(Center.XCenter(colored('│ 3) Если папка src существует то в ней должны находится     │', "yellow")))
    print(Center.XCenter(colored('│ базы в формате name.csv если расширение другое просто      │', "yellow")))
    print(Center.XCenter(colored('│ замените его на .csv  За помощью обращайтесь в бота        │', "yellow")))
    print(Center.XCenter(colored('│ либо лично ко мне                                          │', "yellow")))
    print(Center.XCenter(colored('│ Базы DNS и ZdravSity не подключены, можете пока не качать  │', "yellow")))
    print(Center.XCenter(colored('└────────────────────────────────────────────────────────────┘', "yellow")))
    print(Center.XCenter(colored('┌───────────────────┐     ┌──────────────────────────────────┐', "blue")))
    print(Center.XCenter(colored('│Установка библиотек│  L  │         Установка баз            │', "cyan")))
    print(Center.XCenter(colored('├───────────────────┤  o  ├──────────────────────────────────┤', "blue")))
    print(Center.XCenter(colored('├[L1]socket         |  v  ├[B/D1]ZdravCity(01.2023)   1.16 Гб|', "cyan")))
    print(Center.XCenter(colored('├[L2]requests       |  e  ├[B/D2]Tele2(06.2022)         67 Мб|', "blue")))
    print(Center.XCenter(colored('├[L3]ipaddress      |     ├[B/D3]Паспорта            1 128 Кб|', "cyan")))
    print(Center.XCenter(colored('├[L4]netifaces      |     ├[B/D4]Gemotest             7.76 Гб|', "blue")))
    print(Center.XCenter(colored('├[L5]pyshark        |  i  ├[B/D5]DNS_1 [09.2022]       785 Мб|', "cyan")))
    print(Center.XCenter(colored('├[L6]Tshark         |  s  ├[B/D6]ТГ база 1            1.92 Гб|', "blue")))
    print(Center.XCenter(colored('├[L7]nmap           |     ├[B/D7]ТГ база 2 Глаз Бога  3.33 Мб|', "cyan")))
    print(Center.XCenter(colored('├[L8]scapy          |     ├[B/D8]ТГ база 3 Челябинск  1.30 Мб|', "blue")))
    print(Center.XCenter(colored('├[L9]GDown          |     ├[B/D9]Ru база ФИО-номер    45.9 Мб|', "cyan")))
    print(Center.XCenter(colored('├[L10]PyStile       |     ├[B/D10]Яндекс.еда          3.83 Гб|', "blue")))
    print(Center.XCenter(colored('|                   |  w  |                                  |', "cyan")))
    print(Center.XCenter(colored('├[La]INSTALL ALL    |  a  |[Ba]INSTALL ALL            11.7 Гб|', "blue")))
    print(Center.XCenter(colored('├[b]Вернутся        |  r  |[b]Вернутся                       |', "cyan")))
    print(Center.XCenter(colored('└───────────────────┘     └──────────────────────────────────┘', "blue")))

    install_input = input(Center.XCenter(colored("""\n[+]Select>""", 'red')))


    try: 
        if install_input == 'L1': 
            os.system('pip install socket')
            uclear()
            baners.print_start()
            print(colored('[+]socket установлен', "green")) 
            install()
    except:
        print(colored('[!]socket не установлен', "red"))



    try: 
        if install_input == 'L2': 
            os.system('pip install requests==2.31.0')
            uclear()
            baners.print_start()
            print(colored('[+]requests установлен', "green")) 
            install()
    except:
        print(colored('[!]requests не установлен', "red"))



    try: 
        if install_input == 'L3': 
            os.system('pip install ipaddress')
            uclear()
            baners.print_start()
            print(colored('[+]ipaddress установлен', "green")) 
            install()
    except:
        print(colored('[!]ipaddress не установлен', "red"))



    try: 
        if install_input == 'L4': 
            os.system('pip install netifaces==0.11.0')
            uclear()
            baners.print_start()
            print(colored('[+]netifaces установлен', "green")) 
            install()
    except:
        print(colored('[!]netifaces не установлен', "red"))



    try: 
        if install_input == 'L5': 
            os.system('pip install pyshark==0.6')
            uclear()
            baners.print_start()
            print(colored('[+]pyshark установлен', "green")) 
            install()
    except:
        print(colored('[!]pyshark не установлен', "red"))




    try: 
        if install_input == 'L6': 
            os.system('apt install tshark')
            uclear()
            baners.print_start()
            print(colored('[+]tshark установлен', "green")) 
            install()
    except:
        print(colored('[!]tshark не установлен', "red"))




    try: 
        if install_input == 'L7': 
            os.system('apt install nmap')
            uclear()
            baners.print_start()
            print(colored('[+]nmap установлен', "green")) 
            install()
    except:
        print(colored('[!]nmap не установлен', "red"))



    try: 
        if install_input == 'L8': 
            os.system('pip install scapy')
            uclear()
            baners.print_start()
            print(colored('[+]scapy установлен', "green")) 
            install()
    except:
        print(colored('[!]scapy не уствноылен', "red"))

    try: 
        if install_input == 'L9': 
            os.system('pip install gdown')
            uclear()
            baners.print_start()
            print(colored('[+]GDown установлен', "green")) 
            install()
    except:
        print(colored('[!]GDown не уствноылен', "red"))

    try: 
        if install_input == 'L10': 
            os.system('pip install pystyle')
            uclear()
            baners.print_start()
            print(colored('[+]pystyle установлен', "green")) 
            install()
    except:
        print(colored('[!]pystyle не уствноылен', "red"))

    if install_input == 'La': 
        os.system('pip install socket')             
        os.system('pip install requests==2.31.0')   
        os.system('pip install ipaddress')          
        os.system('pip install netifaces==0.11.0')
        os.system('pip install pyshark==0.6')
        os.system('apt install tshark')
        os.system('apt install nmap')
        os.system('pip install scapy')

        install()

    elif install_input == 'b': 
        main_menu()


    try:
        if install_input == 'B1': 
            download_db('https://drive.google.com/file/d/1gnTbgLgDbYnyVKMHECKM7ic_qb6QKNcr/view?usp=sharing', 'zdravcity.ru_1_01_2023.csv')
            uclear()
            print(colored('zdravcity.ru_1 [01_2023] установлен', "green"))
            install()
    except:
        uclear()
        print(colored('zdravcity.ru_1 [01.2023] не установлен', "red"))
        install()

    try:
        if install_input == 'B2': 
            download_db('https://drive.google.com/file/d/1bxGXVgvroNRdnWZVO9guYWzTD-OHZ48S/view?usp=sharing', 'Tele2.ru (06.2022).csv')
            uclear()
            print(colored('Tele2.ru [06.2022] установлен', "green"))
            install()
    except:
        uclear()
        print(colored('Tele2.ru [06.2022] не установлен', "red"))
        install()

    try:
        if install_input == 'B3': 
            download_db('https://drive.google.com/file/d/18dQSGveWzmKlRCAkVpUq_mtCWUzIHvOU/view?usp=sharing', 'pasports_1.csv')
            uclear()
            print(colored('База паспортов 1 установлена', "green"))
            install()
    except:
        uclear()
        print(colored('База паспортов 1 не установлен', "red"))
        install()

    try:
        if install_input == 'B4': 
            download_db('https://drive.google.com/file/d/1C_jPgbbzirs3a_I0v6w3SIIkmaqZf7w1/view?usp=sharing', 'gemotest.csv')
            uclear()
            print(colored('gemotest установлен', "green"))
            install()
    except:
        uclear()
        print(colored('gemotest не установлен', "red"))
        install()

    try:
        if install_input == 'B5': 
            download_db('https://drive.google.com/file/d/18c6FPV_qD0eZLcFwQXQVqn_i84oeo8hb/view?usp=sharing', 'DNSS_1_09_2022.csv')
            uclear()
            print(colored('DNS [09.2022] установлен', "green"))
            install()
    except:
        uclear()
        print(colored('DNS [09.2022] не установлен', "red"))
        install()

    try:
        if install_input == 'B6': 
            download_db('https://drive.google.com/file/d/138ConTpQAtB43SRAD3Uxh1zMNzqlGXvA/view?usp=sharing', 'tg_base_1.txt')
            uclear()
            print(colored('Telegram база 1 установлена', "green"))
            install()
    except:
        uclear()
        print(colored('Telegram база 1 не установлена', "red"))
        install()

    try:
        if install_input == 'B7': 
            download_db('https://drive.google.com/file/d/1JXmKcbNqQDHw3xUOqigumNewL92e-6Bj/view?usp=sharing', 'tg_base_2(YOG).csv')
            uclear()
            print(colored('Telegram база 2(Глаз бога) установлена', "green"))
            install()
    except:
        uclear()
        print(colored('Telegram база 2(Глаз бога) не установлена', "red"))
        install()

    try:
        if install_input == 'B8': 
            download_db('https://drive.google.com/file/d/1ALni_Pt2qDrUU59uNpSa2MjfKy_EaW0I/view?usp=sharing', 'tg_base_3(chelabinsk).csv')
            uclear()
            print(colored('Telegram база 3(Челябинмк) установлена', "green"))
            install()
    except:
        uclear()
        print(colored('Telegram база 3(Челябинмк) не установлена', "red"))
        install()

    try:
        if install_input == 'B9': 
            download_db('https://drive.google.com/file/d/15WI8rEM5SLXdLQGjxi0DMQspGZpqgtjB/view?usp=sharing', 'ru_base.csv')
            uclear()
            print(colored('База установлена', "green"))
            install()
    except:
        uclear()
        print(colored('База не установлена', "red"))
        install()

    try:
        if install_input == 'B10': 
            download_db('https://drive.google.com/file/d/1_M1IqS4OeHJAAB1GcQrT25cY49mr2vFW/view?usp=sharing', 'YaEda_1.csv') 
            download_db('https://drive.google.com/file/d/1xvbA5X-tJzQ5RGeqChOJuo1TKwD1YKVB/view?usp=sharing', 'YaEda_2.csv')
            download_db('https://drive.google.com/file/d/1-xPkLKYRKDI1pkUkukEoFU29mgjSVuri/view?usp=sharing', 'YaEda_3.csv')
            download_db('https://drive.google.com/file/d/1CAKT4VngYQpKifXM8kRqNsQ401RWszWC/view?usp=sharing', 'YaEda_4.csv')
            download_db('https://drive.google.com/file/d/1IBWaz4lND3FAYLRNiCMQjGi5NGuSGi9b/view?usp=sharing', 'YaEda_5.csv')
            #5
            download_db('https://drive.google.com/file/d/125yAu32QulgO31Paz2LOzO_BdFxZ8IYy/view?usp=sharing', 'YaEda_6.csv')
            download_db('https://drive.google.com/file/d/1XDlslRSNhRJbQSJdOGulfpOCD_I31O1V/view?usp=sharing', 'YaEda_7.csv')
            download_db('https://drive.google.com/file/d/1X244yUx7rDTSKhLI6WJp1pRRHHKMe7hS/view?usp=sharing', 'YaEda_8.csv')
            download_db('https://drive.google.com/file/d/13q-9lNNPvxLotwOHUlkpSOApROgaDq2e/view?usp=sharing', 'YaEda_9.csv')
            download_db('https://drive.google.com/file/d/15LVf5H77KecrzPQ7SY3B6FfAX0Go82kr/view?usp=sharing', 'YaEda_10.csv')
            #10
            download_db('https://drive.google.com/file/d/1OETFFZC8qO4zsXGJIez835He4Hporlgb/view?usp=sharing', 'YaEda_11.csv')
            download_db('https://drive.google.com/file/d/19POMnOYWfNGYbaeZDBV0kWxxZUq1Ujm_/view?usp=sharing', 'YaEda_12.csv')
            download_db('https://drive.google.com/file/d/1pkt-NupEuBYSYSxvDcUgt9QDdjgxIS_o/view?usp=sharing', 'YaEda_13.csv')
            download_db('https://drive.google.com/file/d/10BNhBbHdtIKE_iX4aCzHVmhHzESr-u01/view?usp=sharing', 'YaEda_14.csv')
            download_db('https://drive.google.com/file/d/1eKdjTEJNz6p1pglj1XVD1N_20rdFbZ48/view?usp=sharing', 'YaEda_15.csv')
            #15
            download_db('https://drive.google.com/file/d/1aOnhedikZMqtzwyReZ4Ho-1M3OyXwP1r/view?usp=sharing', 'YaEda_16.csv')
            download_db('https://drive.google.com/file/d/1AgvfZYyjlJtlubbBYMMNGlyTfMMvHuL4/view?usp=sharing', 'YaEda_17.csv')
            download_db('https://drive.google.com/file/d/1DmiakC-vOUxuE7lFe5QMNnyp0qM-MTwU/view?usp=sharing', 'YaEda_18.csv')
            download_db('https://drive.google.com/file/d/1v-h2uL4ZCixG0G1wR_Q0HOwudyvkTOOd/view?usp=sharing', 'YaEda_19.csv')
            download_db('https://drive.google.com/file/d/1qqFLTKZOnWJJTZrm5qKfsc0f3jxAZ_P5/view?usp=sharing', 'YaEda_20.csv')
            #20
            download_db('https://drive.google.com/file/d/1GJluxCkiAPul6Q_qmEMDnaTpl2jNjkSx/view?usp=sharing', 'YaEda_21.csv')
            download_db('https://drive.google.com/file/d/1hiPRfqKzhZQWiW3cq1lN6fXiE01qbX7y/view?usp=sharing', 'YaEda_22.csv')
            download_db('https://drive.google.com/file/d/1N0jFGbSPYzYIaDo0_LcKtzlB9N5IZiXb/view?usp=sharing', 'YaEda_23.csv')
            download_db('https://drive.google.com/file/d/1i1xjR54LmyfAP-oqdvb6Zn8TKuFNUu1C/view?usp=sharing', 'YaEda_24.csv')
            download_db('https://drive.google.com/file/d/1i1xjR54LmyfAP-oqdvb6Zn8TKuFNUu1C/view?usp=sharing', 'YaEda_25.csv')
            #25
            download_db('https://drive.google.com/file/d/1PB4FXHlyZ8UOqXx87KL3xZigdAol93ic/view?usp=sharing', 'YaEda_26.csv')
            download_db('https://drive.google.com/file/d/1SmOm2pTXOBSiF0Ie-2j3eXc3hUrmw2It/view?usp=sharing', 'YaEda_27.csv')
            download_db('https://drive.google.com/file/d/1oyvhVP1ONnj9KM8_fqTzaIX1qxDcBAEG/view?usp=sharing', 'YaEda_28.csv')
            download_db('https://drive.google.com/file/d/1a6IcKq_p29ym6KwBc034wsrfOj9tkGFr/view?usp=sharing', 'YaEda_29.csv')
            download_db('https://drive.google.com/file/d/1VD1Mp-kTDBCNbcYhsYPKcVq4aSn9asvC/view?usp=sharing', 'YaEda_30.csv')
            #30
            download_db('https://drive.google.com/file/d/1xQLymeyTjiG08Z5cOjqMn0F3kETgVCRY/view?usp=sharing', 'YaEda_31.csv')
            download_db('https://drive.google.com/file/d/13SfrzrFQ2xt-ADDOMkepqeVej2DiGZbn/view?usp=sharing', 'YaEda_32.csv')
            download_db('https://drive.google.com/file/d/1E6ORbSvt5V4bRuDTXXrDTnnFk9XdAdao/view?usp=sharing', 'YaEda_33.csv')
            download_db('https://drive.google.com/file/d/12u3E_dwPYmsir5k_b8TztdgUq523rP5T/view?usp=sharing', 'YaEda_34.csv')
            download_db('https://drive.google.com/file/d/1TG6vdgeqXZTi-6G84KXgAqS4ahSYWrRj/view?usp=sharing', 'YaEda_35.csv')
            #35
            download_db('https://drive.google.com/file/d/10wZQqvw51qJhkyRd9kgMNNI_4m8XeH35/view?usp=sharing', 'YaEda_36.csv')
            download_db('https://drive.google.com/file/d/1W7-TFdOHfsUlO9hMc3vrwLxqcDD3qMNC/view?usp=sharing', 'YaEda_37.csv')
            download_db('https://drive.google.com/file/d/1xMdM9rB-XzgRJIJrQ82KvehuTkGTqut_/view?usp=sharing', 'YaEda_38.csv')
            download_db('https://drive.google.com/file/d/13yY-dOi2HZQfMHH-fdBBf4kLtmChbaUh/view?usp=sharing', 'YaEda_39.csv')
            download_db('https://drive.google.com/file/d/1zkH1ZYjV3aF7rFAih8p2bH52ojn3X3oy/view?usp=sharing', 'YaEda_40.csv')
            #40
            download_db('https://drive.google.com/file/d/10lEf2d70B77z9Y8JXHxb2IHXM3j7qpQo/view?usp=sharing', 'YaEda_41.csv')
            download_db('https://drive.google.com/file/d/1JuuzCodOyeofQLEkEB1uaimNzQbtzw36/view?usp=sharing', 'YaEda_42.csv')
            download_db('https://drive.google.com/file/d/1SE_8NQsALWWE-ycUxjkgP_Ktmg7qrJ0q/view?usp=sharing', 'YaEda_43.csv')
            download_db('https://drive.google.com/file/d/1DVjvPtQVWGHdsHeMkm2nIXJFAyIfO7no/view?usp=sharing', 'YaEda_44.csv')
            download_db('https://drive.google.com/file/d/1a-U_d7HBB7I4bUMIgrnZRtKFzgzoLxBG/view?usp=sharing', 'YaEda_45.csv')
            #45
            download_db('https://drive.google.com/file/d/1nA6IsXSq5Pk4kRpoEwISiSFlWncemdci/view?usp=sharing', 'YaEda_46.csv')
            download_db('https://drive.google.com/file/d/1q_sugn4LsBYrRgsptRMtkkB7b3RWsZH1/view?usp=sharing', 'YaEda_47.csv')
            download_db('https://drive.google.com/file/d/1iHU-2LHkf0H_APadYRcVPbDbrn9TAPXg/view?usp=sharing', 'YaEda_48.csv')
            download_db('https://drive.google.com/file/d/1cr60kZDqkszyIhMTr3Em2_UKKlkuY9Vv/view?usp=sharing', 'YaEda_49.csv')
            download_db('https://drive.google.com/file/d/1QqZzhqeMmG-lc5SiWA1bBYeifxKQBVYd/view?usp=sharing', 'YaEda_ekaterinburg')
            #50
            download_db('https://drive.google.com/file/d/1-DIm2PsJE3nwQZCTxsBFSru_vr6chDSI/view?usp=sharing', 'YaEda_kazan')
            download_db('https://drive.google.com/file/d/1LPl90B6PT54cpPfwQXB62oIkrocdzYSO/view?usp=sharing', 'YaEda_krasnodar')
            download_db('https://drive.google.com/file/d/1nERB7f_OgJunFT5l2UN1h5EW2t264bVD/view?usp=sharing', 'YaEda_moscpw_1')
            download_db('https://drive.google.com/file/d/1TMLD00s73ScWDgkFuprSHtaIdOiO5A-2/view?usp=sharing', 'YaEda_moscpw_2')
            download_db('https://drive.google.com/file/d/1sbapo48CtLljXBsSPCX9ZmEISnyCZ7UQ/view?usp=sharing', 'YaEda_moscpw_3')
            #55
            download_db('https://drive.google.com/file/d/1j3ojwTP40azC1hvPdFq761kssc7Drw-E/view?usp=sharing', 'YaEda_nizniy_novgorod')
            download_db('https://drive.google.com/file/d/1azp1y2bPpfpFcanhTyIo53oa5U0fLSs6/view?usp=sharing', 'YaEda_spb_3')
            download_db('https://drive.google.com/file/d/1Bb6WqSrqXS73OY1HX5TY-Mn4oSRi5z_J/view?usp=sharing', 'YaEda_rostov_na_donu')
            download_db('https://drive.google.com/file/d/1CsnL43DZ395mNfvq7duPWrKcR8HYGUTP/view?usp=sharing', 'YaEda_samara')
            download_db('https://drive.google.com/file/d/10tc1CPdlcESyEl8W-tzH5sD5ciyd1lC5/view?usp=sharing', 'YaEda_ufa')
            #60
            download_db('https://drive.google.com/file/d/1ZvNDMmus8hbqrFXk_l9XKoIJihHlK_1X/view?usp=sharing', 'YaEda_voronej')
            
            uclear()
            print(colored('База установлена', "green"))
            install()
    except:
        uclear()
        print(colored('База не установлена', "red"))
        install()

    if install_input == 'D1': del_db('zdravcity.ru_1_01_2023.csv')
    elif install_input == 'D2': del_db('Tele2.ru (06.2022).csv')
    elif install_input == 'D3': del_db('pasports_1.csv')
    elif install_input == 'D4': del_db('gemotest.csv')
    elif install_input == 'D5': del_db('DNSS_1_09_2022.csv')
    elif install_input == 'D6': del_db('tg_base_1.txt')
    elif install_input == 'D7': del_db('tg_base_2(YOG).csv')
    elif install_input == 'D8': del_db('tg_base_3(chelabinsk).csv')
    elif install_input == 'D9': del_db('ru_base.csv')

    

def main_menu():
    baners.print_start()
    mm_1 =  colored('┌────────────────────────────────────────────────────┐', "red").center(20)
    mm_2 =  colored('|                    Главное Меню                    |', "red")
    mm_3 =  colored('├──────────────────────────┬─────────────────────────┤', "red")
    mm_4 =  colored('├[e] - exit                ├[i] - info               |', "red")
    mm_5 =  colored('├[s] - setings             ├[d] - install            |', "red")
    mm_6 =  colored('├[1] - Узнать ip telegram  ├[6] - WiFite 3           |', "cyan")
    mm_7 =  colored('├[2] - Сканер портов       ├[7] - Пробив по базам    |', 'blue')
    mm_8 =  colored('├[3] - SMS-Bomber          ├[8] - DDoS               |', 'cyan')
    mm_9 =  colored('├[4] - FlipperNull         ├[9] - AirDos             |', 'blue')
    mm_10 = colored('├[5] - SQLmap              ├[10] - ???               |', 'cyan')
    mm_11 = colored('└──────────────────────────┸─────────────────────────┘', "blue")
    
    print(Center.XCenter(mm_1))
    print(Center.XCenter(mm_2))
    print(Center.XCenter(mm_3))
    print(Center.XCenter(mm_4))
    print(Center.XCenter(mm_5))
    print(Center.XCenter(mm_6))
    print(Center.XCenter(mm_7))
    print(Center.XCenter(mm_8))
    print(Center.XCenter(mm_9))
    print(Center.XCenter(mm_10))
    print(Center.XCenter(mm_11))

    print('')
	
    #input_text = Center.XCenter()"""\n[+]> """, "red"
    select = input(Center.XCenter(colored("""\n[+]Select> """, "red")))

    
#################################################

    if select == '1': 
        from tgip import main
        uclear()
        baners.print_start()
        main()
                    
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye
            exit
	
#################################################

    elif select == '2':
        import port_scan
        port_scan.main()

        print(Center.XCenter(colored('   ╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('   ║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('   ║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('   ╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye
            exit
        
#################################################

    elif select == '3':
        from bomber import start_bomber
        uclear()
        baners.print_start()
        start_bomber()
            
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye
            exit

#################################################

    elif select == '4':
        from FlipperNull import FlipperNull
        uclear()
        baners.print_start()
        FlipperNull()
            
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye
            exit

#################################################

    elif select == '5':
        print(colored('[!]В разарботке', "red"))
            
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye
            exit

#################################################

    elif select == '6':
        uclear()
        start_serch()
            
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit

#################################################

    elif select == '7':
        uclear()
        start_serch()
            
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit

#################################################

    elif select == '8':
        import ddos
        uclear()
        ddos.start_DDoS()
            
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit

#################################################

    elif select == '9':
        print(colored('[!]В разарботке', "red"))
            
        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit

#################################################

    elif select == '10':
        with open('data.pkl', 'rb') as file:
            data = pickle.load(file)  
            print(data['devise'])

        print(Center.XCenter(colored('╔══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║[1] - Вернутся в меню ║', "cyan")))
        print(Center.XCenter(colored('║[2] - Выход           ║', "cyan")))
        print(Center.XCenter(colored('╚══════════════════════╝', "cyan")))

        mrnu_or_exit = input(Center.XCenter(colored("""\n[+]Select>""", 'cyan')))

        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit


#################################################

    elif select == 's':
        setings()

    elif select == 'd':
        install()

    elif select == 'i': 
        baners.soft_info()
        main_menu()

    elif select == 'e':
        baners.print_bye_bye()
        sys.exit()

    
    else: 
        uclear()
        main_menu()

osname = os.name
if osname == 'nt':
    os.system('DEL defolt_set.py')
    os.system('DEL base_creater.py')
    os.system('DEL data.pkl')
elif osname == 'posix':
    os.system('rm -rf defolt_set.py')
    os.system('rm -rf base_creater.py')
    os.system('rm -rf data.pkl')


uclear()
print('\n\n\n\n\n\n\n\n\n')
print(Center.XCenter(colored('╔═════════════════════════════════════════════════════════════╗', 'yellow')))
print(Center.XCenter(colored('║                         ИНФОРМАЦИЯ                          ║', 'yellow')))
print(Center.XCenter(colored('╠═════════════════════════════════════════════════════════════╣', 'yellow')))
print(Center.XCenter(colored('║Имея данный софт вы обязаны соблюдать следующие правила      ║', 'yellow')))
print(Center.XCenter(colored('║                                                             ║', 'yellow')))
print(Center.XCenter(colored('║1)Принимаете ответственность за все свои действия на себя.   ║', 'yellow')))
print(Center.XCenter(colored('║2)Обязуетесь в случае публикованиях программы на различных   ║', 'yellow')))
print(Center.XCenter(colored('║информационных информационных ресурсов указывать тгк автора  ║', 'yellow')))
print(Center.XCenter(colored('║https://t.me/ziyou_off   либо  https://t.me/+To5Lgt_Fx70zZDMy║', 'yellow')))
print(Center.XCenter(colored('║3)Не выодовать себя за автора программы                      ║', 'yellow')))
print(Center.XCenter(colored('║4)Так же категорически запрещается продавть данную программу ║', 'yellow')))
print(Center.XCenter(colored('╚═════════════════════════════════════════════════════════════╝', 'yellow')))
print('\n\n\n')
print(Center.XCenter(colored('╔═══════════════════════════════════════════════════╗', 'red')))
print(Center.XCenter(colored('║Ведите [L] Чтобы открыть официльный канал c паролем║', 'red')))
print(Center.XCenter(colored('╚═══════════════════════════════════════════════════╝', 'red')))                             
print('\n\n\n')                            
in_pw = input(Center.XCenter(colored('[@]ВВЕДИТЕ ПАРОЛЬ: ', 'red')))
if in_pw == 'pepe776':

    try:
        with open('save', 'rb') as file:
            data = pickle.load(file)
    except:
        data = {'devise': 'M',
                'base_out': 'T',
                'hello_anim': '1'}
        
        with open("save","wb") as save:
            pickle.dump(data,save)
        
    baners.print_hello()
    uclear()
    main_menu()

elif in_pw == 'L':
    webbrowser.open("https://t.me/+To5Lgt_Fx70zZDMy")

elif in_pw == 'E':
    uclear()
    sys.exit()

else:
    uclear()
    print(Center.XCenter(Center.YCenter(colored('╔═════════════════════╗', 'red'))))
    print(Center.XCenter(colored('║[!]НЕВЕРНЫЙ ПАРОЛЬ!!!║', 'red')))
    print(Center.XCenter(colored('╚═════════════════════╝', 'red')))
    sys.exit()
    
