from termcolor import colored
import time
import os

os.system('clear')


def baner():
    print(colored(""".
⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⠟⠋⠉⠁⠁⠁⠀⠀⣄⣀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠉⠉⠛⠟⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡇⠀⠀⣀⣄⠀⢹⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣿⣿⣿⣿
⠛⢀⣠⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠀⠀⠀⢿⣷⣶⣾⣿⣿⣿⡟⠁⠸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⡄⠀⢲⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣸⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠊⠂⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⣀⣀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡄⠀⠘⠉⢡⣄⡈⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣄⠀⠀⠀⣠⠀⠀⠀⠀⣤⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⡀⠛⠋⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣿⣿⣿⣆⠀⢸⣿⣶⠀⠀⣠⡿⠦⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣷⣤⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣷⣾⣿⣧⠀⠀⠋⠀⠀⠃⡾⠻⠿⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⡀⠀⠀⠀⢳⢤⠀⠀⠹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⡘⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠁⠀⠁⠈⣶⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣅⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⣀⣀⣤⡀⠀⠀⢀⣼⣿⣿⠛
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⣶⣿⠟⠋⢉⣤
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿
""", "blue"))
    print(colored("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""░░░░░░░░░░░░░░░░░______░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""░░░░░░░░░░░░░░░░|__   (_)_   _  ___  _   _ ░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""░░░░░░░░░░░░░░░░░░░/ /| | | | |/ _ \| | | |░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""░░░░░░░░░░░░░░░░░░/ /_| | |_| | (_) | |_| |░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""░░░░░░░░░░░░░░░░░/____|_|\__, |\___/ \__,_|░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""░░░░░░░░░░░░░░░░░░░░░░░░░|___/░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""", "yellow"))
    print(colored("""                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄""", "yellow"))
    print(colored("""                ▄Telegtam: @ziyouoff▄""", "yellow"))
    print(colored("""                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄""", "yellow"))

def soft_info():
    print(f'''Хей с вами ZiYou, мой софт пишится и мобирает другие утилиты только с благими намерниями как и те инструменты которые я использую
Думаю надо все же назвть людей чьи куски кода я использовал
n0a, cпасибо за понятные объяснение и кусочки когда зоть и врядле ты увидишь это сообщение''')
    time.sleep(3)


def main_menu():
    baner()
    print('[0] - Информация')
    print('[1] - Узнать ip telegram')
    print('[2] - Сканер портов')
    print('[3] - SMS-Bomber')
    print(colored('[4] - FlipperNull', 'yellow'))
    print('[4] - SQLmap...(В РАЗРАБОТКЕ)')
    print('')
    print(colored('[e] - Выход', "red"))
	
    select = input(colored("""\n[+]> """, "red"))

    if select == '0': 
        soft_info()
        main_menu()

    elif select == '1': 
        from tgip import main
        os.system('clear')
        baner()
        main()
        
        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input()
        if mrnu_or_exit == '1':
            baner()
            main_menu()

        elif mrnu_or_exit == '2':
            exit
	
    elif select == '2':
        from port_scan import main
        main()
        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baner()
            main_menu()

        elif mrnu_or_exit == '2':
            exit
        


    elif select == '3':
        from bomber import start_bomber
        os.system('clear')
        baner()
        start_bomber()

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baner()
            main_menu()

        elif mrnu_or_exit == '2':
            exit

    
    elif select == '4':
        from FlipperNull import FlipperNull
        os.system('clear')
        baner()
        FlipperNull()

        print(colored('[1] - Вернутся в меню\n[2] - Выход', "cyan"))
        mrnu_or_exit = input(colored("""\n[+]>""", 'cyan'))
        if mrnu_or_exit == '1':
            baner()
            main_menu()

        elif mrnu_or_exit == '2':
            exit




    elif select == 'e' or 'E':
        exit


    else: 
        os.system('clear')
        main_menu()

main_menu()