import os 
import pickle
import baners
import main

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


############################################################
############################################################
############################################################
if os.path.exists('data.pkl'):
    # Восстановление переменных
    with open('data.pkl', 'rb') as file:
        restored_data = pickle.load(file)
    print(restored_data)
    
else:
    # Сохранение переменных
    data = {'devise': 'M'}
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)
    
def setings():
    baners.print_ascll_setings()

    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)
        devise = data['devise']

    print(Center.XCenter(colored('┌──────────────────────────────────┐', "yellow")))
    print(Center.XCenter(colored('|            Настройки             |', "yellow")))
    print(Center.XCenter(colored('├──────────────────────────────────┤', "yellow")))
    print(Center.XCenter(colored('├[1] - Выбрать Устройство       [' + devise + ']│', "yellow"))) 
    print(Center.XCenter(colored('│                                  │', "yellow"))) 
    print(Center.XCenter(colored('├[b] - Назад                       │', "yellow"))) 
    print(Center.XCenter(colored('└──────────────────────────────────┘', "yellow")))

    select = input(Center.XCenter(colored("""\n[+]select > """, "red")))

    if select == '1':

        print(Center.XCenter(colored('┌──────────────────────────────────┐', "yellow")))
        print(Center.XCenter(colored('│"M" - Мобильный вид софта         │', "yellow")))
        print(Center.XCenter(colored('│"P" - Вид софта софта для PC      │', "yellow")))
        print(Center.XCenter(colored('└──────────────────────────────────┘', "yellow")))

        select = input(Center.XCenter(colored("""\n[+]select > """, "red")))

        if select == 'M':
            data['devise'] = 'M'
            with open('data.pkl', 'wb') as file:
                pickle.dump(data, file)

        elif select == 'P':
            data['devise'] = 'P'
            with open('data.pkl', 'wb') as file:
                pickle.dump(data, file)

    elif select == 'b':
        main_menu()

     

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
    serch_name.tele2_1_06_22(fio)
    serch_name.zdravcity_1_01_23(fio)
    serch_name.gemotest(fio)
    serch_name.ru_base(fio)

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
    baners.print_start()
    print(Center.XCenter(colored('┌──────────────────────────────────┐', "yellow")))
    print(Center.XCenter(colored('├[1] - Поиск по номеру             │', "yellow")))
    print(Center.XCenter(colored('├[2] - Поиск по имени              │', "yellow")))
    print(Center.XCenter(colored('├[3] - Поиск по user_name telegram │', "yellow")))
    print(Center.XCenter(colored('│                                  │', "yellow")))
    print(Center.XCenter(colored('├[b] - Вернутся                    │', "yellow")))
    print(Center.XCenter(colored('└──────────────────────────────────┘', "yellow")))

    select_info_type = input(colored("""\n[+]>""", 'cyan'))

    if select_info_type == '1': start_serch_phone()
    elif select_info_type == '2': start_serch_name()
    elif select_info_type == '3': start_serch_telegram()

    elif select_info_type == 'b': main_menu()

############################################################
############################################################
############################################################

def install():
    if os.path.exists("src/"):
        print("Файл существует")
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
    print(Center.XCenter(colored('│ 1) При отсутсвии папки src просто создайте ее              │', "yellow")))
    print(Center.XCenter(colored('│ 2) Если папка src существует то в ней должны находится     │', "yellow")))
    print(Center.XCenter(colored('│ базы в формате name.csv если расширение другое просто      │', "yellow")))
    print(Center.XCenter(colored('│ замените его на .csv  За помощью обращайтесь в бота        │', "yellow")))
    print(Center.XCenter(colored('│ либо лично ко мне                                          │', "yellow")))
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
    print(Center.XCenter(colored('├[L10]PyStile       |     |                                  |', "blue")))
    print(Center.XCenter(colored('|                   |  w  |                                  |', "cyan")))
    print(Center.XCenter(colored('├[La]INSTALL ALL    |  a  |[Ba]INSTALL ALL            11.7 Гб|', "blue")))
    print(Center.XCenter(colored('├[b]Вернутся        |  r  |[b]Вернутся                       |', "cyan")))
    print(Center.XCenter(colored('└───────────────────┘     └──────────────────────────────────┘', "blue")))
    print(Center.XCenter('Пссс... Базы DNS и ZdravSity не подключены, можете пока не качать'))

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
    select = input(Center.XCenter(colored("""\n[+]> """, "red")))

    
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
        with open('data.pkl', 'rb') as file:
            data = pickle.load(file)  
            print(data['devise'])
         
        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
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
        exit

    
    else: 
        uclear()
        main_menu()
  

main_menu()