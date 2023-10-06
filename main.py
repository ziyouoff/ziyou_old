from termcolor import colored
import time
import baners
import os




def main_menu():
    baners.print_start()
    print(colored('[e] - exit                |          [0] - info', "red"))
    print(colored('[1] - Узнать ip telegram  |          [6] - Telegram user id', "cyan"))
    print(colored('[2] - Сканер портов       |          [7] - Пробив по номеру', 'blue'))
    print(colored('[3] - SMS-Bomber          |          [8] - DDoS', 'cyan'))
    print(colored('[4] - FlipperNull         |          [9] - AirDos', 'blue'))
    print(colored('[5] - SQLmap              |          [10] - ', 'cyan'))

    print('')
	
    select = input(colored("""\n[+]> """, "red"))

    
#################################################

    if select == '1': 
        from tgip import main
        os.system('clear')
        baners.print_start()
        main()
        
        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
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
            exit
        
#################################################

    elif select == '3':
        from bomber import start_bomber
        os.system('clear')
        baners.print_start()
        start_bomber()

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            exit

#################################################

    elif select == '4':
        from FlipperNull import FlipperNull
        os.system('clear')
        baners.print_start()
        FlipperNull()

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            exit

#################################################

    elif select == '6':
        import tgtonum
        tgtonum.tgtonum()

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baners.print_start()
            main_menu()

        elif mrnu_or_exit == '2':
            exit


    elif select == '0': 
        baners.soft_info()
        main_menu()
    elif select == 'e' or 'E':
        exit

    else: 
        os.system('clear')
        main_menu()

main_menu()