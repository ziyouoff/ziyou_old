import os
import baners
import gdown

try:
    from termcolor import colored
except:
    os.system('pip install termcolor')



def download_db(URL, NAME):
    output_file = os.path.dirname(os.path.abspath(__file__))
    output_file = output_file + "\src\\" + NAME

    gdown.download(URL, output_file, quiet=False, fuzzy=True)
    
    


def uclear():
    osname = os.name
    if osname == 'nt': os.system('cls')
    elif osname == 'posix': os.system('clear')

############################################################
############################################################
############################################################

def start_serch_name():
    import serch_name
    fio = input(colored("[+]Введите имя: ", "cyan"))

    serch_name.pasports_1(fio)

##############################

def start_serch_phone():
    import serch_phone
    phone = input(colored("[+]Введите номер телефона для поиска(без +): ", "cyan"))
    
    serch_phone.tele2_1_06_22(phone)
    serch_phone.zdravcity_1_01_23(phone)
    serch_phone.DNSS_1_09_2022(phone)
    serch_phone.gemotest(phone)

##############################

def start_serch_telegram():
    import serch_telegram
    print(colored(baners.telegram_logo, "cyan"))
    uid = input(colored("[+]Введите user_name пользователя: ", "cyan"))

    serch_telegram.find_phone_by_uid_1(uid)
    serch_telegram.find_phone_by_uid_2(uid)
    serch_telegram.find_phone_by_uid_3(uid)
    

##############################

def start_serch():
    print(colored('┌──────────────────────────────────┐', "yellow"))
    print(colored('├[1] - Поиск по номеру             │', "yellow"))
    print(colored('├[2] - Поиск по имени              │', "yellow"))
    print(colored('├[3] - Поиск по user_name telegram │', "yellow"))
    print(colored('│                                  │', "yellow"))
    print(colored('├[b] - Вернутся                    │', "yellow"))
    print(colored('└──────────────────────────────────┘', "yellow"))

    select_info_type = input(colored("""\n[+]>""", 'cyan'))

    if select_info_type == '1': start_serch_phone()
    elif select_info_type == '2': start_serch_name()
    elif select_info_type == '3': start_serch_telegram()

    elif select_info_type == 'b': main_menu()

############################################################
############################################################
############################################################

def install():
    print(colored('┌───────────────────┐     ┌───────────────────────┐', "green"))
    print(colored('│Установка библиотек│     │     Установка баз     │', "light_green"))
    print(colored('├───────────────────┤     ├───────────────────────┤', "green"))
    print(colored('├[L1]socket         |     ├[B1]ZdravCity(01.2023) |', "light_green"))
    print(colored('├[L2]requests       |     ├[B2]Tele2(06.2022)     |', "green"))
    print(colored('├[L3]ipaddress      |     ├[B3]Паспорта 1         |', "light_green"))
    print(colored('├[L4]netifaces      |     ├[B4]Gemotest           |', "green"))
    print(colored('├[L5]pyshark        |     ├[B5]DNS_1 (09.2022)    |', "light_green"))
    print(colored('├[L6]Tshark         |     ├[B6]ТГ база 1          |', "green"))
    print(colored('├[L7]nmap           |     ├[B7]ТГ база 2 Глаз Бога|', "light_green"))
    print(colored('├[L8]scapy          |     ├[B8]ТГ база 3 Челябинск|', "green"))
    print(colored('├[L9]GDown          |     |                       |', "light_green"))
    print(colored('|                   |     |                       |', "green"))
    print(colored('├[La]INSTALL ALL    |     |[Ba]INSTALL ALL        |', "light_green"))
    print(colored('├[b]Вернутся        |     |[b]Вернутся            |', "green"))
    print(colored('└───────────────────┘     └───────────────────────┘', "light_green"))
    print('Пссс... Базы DNS и ZdravSity не подключены, можете пока не качать')

    install_input = input(colored("""\n[+]> """, "red"))

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

    
    
    
    



    

def main_menu():
    baners.print_start()
    main_menu_up = colored('┌──────────────────────────┬─────────────────────────┐', "red")
    main_menu_ei = colored('├[e] - exit                ├[i] - info               |', "red")
    main_menu_sd = colored('├[s] - setings             ├[d] - install            |', "red")
    main_menu_16 = colored('├[1] - Узнать ip telegram  ├[6] - ???                |', "cyan")
    main_menu_27 = colored('├[2] - Сканер портов       ├[7] - Пробив по базам    |', 'blue')
    main_menu_38 = colored('├[3] - SMS-Bomber          ├[8] - DDoS               |', 'cyan')
    main_menu_49 = colored('├[4] - FlipperNull         ├[9] - AirDos             |', 'blue')
    main_menu_50 = colored('├[5] - SQLmap              ├[10] - ???               |', 'cyan')
    main_menu_dn = colored('└──────────────────────────┸─────────────────────────┘', "blue")

    print(main_menu_up)
    print(main_menu_ei)
    print(main_menu_sd)
    print(main_menu_16)
    print(main_menu_27)
    print(main_menu_38)
    print(main_menu_49)
    print(main_menu_50)
    print(main_menu_dn)
    

    print('')
	
    select = input(colored("""\n[+]> """, "red"))

    
#################################################

    if select == '1': 
        from tgip import main
        uclear()
        baners.print_start()
        main()
        
        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye
            exit
	
#################################################

    elif select == '2':
        from port_scan import main
        main()
        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
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

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
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

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye
            exit

#################################################

    elif select == '5':
        print(colored('[!]В разарботке', "red"))

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
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

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
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

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
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

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit

#################################################

    elif select == '9':
        print(colored('[!]В разарботке', "red"))

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit

#################################################

    elif select == '10':
        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            baners.print_bye_bye()
            exit


#################################################

    elif select == 'd':
        install()


    elif select == 'i': 
        baners.soft_info()
        main_menu()

    elif select == 'e':
        baners.print_bye_bye()
        exit

    
    else: 
        uclear()
        main_menu()

main_menu()