from termcolor import colored
import main
import os
try:
    from rich.console import Console
    from rich.table import Table
    from rich.tree import Tree
    from rich import print as rprint
except:
    os.system('pip install Rich')
    from rich.console import Console
    from rich.table import Table
    from rich.tree import Tree
    from rich import print as rprint

try:
    from pystyle import Center
except:
    os.system('pip install pystyle')
    from pystyle import Center

table = Table()

table.add_column("Название базы", style='green')
table.add_column("ФИО", style="blue")
table.add_column("Номер телефона", style="cyan")
table.add_column("Дата рождения", style="blue")
table.add_column("Адрес", style="magenta")
table.add_column("Почта", style='blue')
table.add_column("Паспорт", style='cyan')
table.add_column("Выдан кем", style="blue")

def tele2_1_06_22(phone):
    try:
        with open('src//Tele2.ru (06.2022).csv', 'r', encoding='utf-8') as file:        
            for line in file:
                #print(line)
                data = line.strip().split(';')  
                if len(data) >= 3 and data[2] == phone:
                    if main.data['base_out'] == 'T':
                        print('\n')
                        tree_tele_2 = Tree('Tele2 [06.2022]', style='red')
                        tree_tele_2.add('Почта', style='cyan').add(str(data[0].strip()), style='yellow')
                        tree_tele_2.add('ФИО', style='cyan').add(str(data[1].strip()), style='yellow')
                        tree_tele_2.add('Номер телефона', style='cyan').add(str(data[2].strip()), style='yellow')
                        rprint(tree_tele_2)
                    elif main.data['base_out'] == 'S':
                        print(colored('┌──────────────────────────────────────────────────────', "green"))
                        print(colored('│Найдено в базе Tele2 [06.2022]', "green"))
                        print(colored('├──────────────────────────────────────────────────────', "green"))
                        print(colored('├Почта: ' + data[0].strip(), "green"))
                        print(colored('├ФИО: ' + data[1].strip(), "green"))
                        print(colored('├Номер телефона: ' + data[2].strip(), "green"))
                        print(colored('└──────────────────────────────────────────────────────', "green"))

                    table.add_row('Tele2 [06.2022]',str(data[1].strip()), str(data[2].strip()), '-', '-', str(data[1].strip()), '-', '-')

        print(colored(f"Номер телефона в 1-ой базе не найден :( ", "red"))
    except:
        print(colored('База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))

##########################################################################################################
def zdravcity_1_01_23(phone):
    try:
        with open('src//zdravcity.ru_1_01_2023.csv', 'r', encoding='utf-8') as file:        
            for line in file:
                #print(line)
                data = line.strip().split('		')  
                if len(data) >= 8 and data[0] == phone:
                    print(colored('┌──────────────────────────────────────────────────────', "green"))
                    print(colored('│Найдено в базе zdravcity(01.1023)', "green"))
                    print(colored('├──────────────────────────────────────────────────────', "green"))
                    print(colored('├Номер Телефона: ' + data[0].strip(), "green"))
                    print(colored('├Почта: ' + data[1].strip(), "green"))
                    print(colored('├ФИО: ' + data[2].strip(), "green"))
                    print(colored('├Дата рождения: ' + data[3].strip(), "green"))
                    print(colored('├Пол: ' + data[7].strip(), "green"))
                    print(colored('├Адрес: ' + data[8].strip(), "green"))
                    print(colored('└──────────────────────────────────────────────────────', "green"))

        print(colored(f"Номер телефона во 2-ой базе не найден :( ", "red"))
    except:
        print(colored('База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))

##########################################################################################################
def DNSS_1_09_2022 (phone):
    try:
        with open('src//DNSS_1_09_2022.csv', 'r', encoding='utf-8') as file:        
            for line in file:
                data = line.strip().split(';')  
                if len(data) >= 8 and data[1] == phone:
                    print(colored('┌──────────────────────────────────────────────────────', "green"))
                    print(colored('│Найдено в базе DNS(09.2022)', "green"))
                    print(colored('├──────────────────────────────────────────────────────', "green"))
                    print(colored('├Ник: ' + data[0].strip(), "green"))
                    print(colored('├Номер: ' + data[1].strip(), "green"))
                    print(colored('├Почта: ' + data[2].strip(), "green"))
                    print(colored('└──────────────────────────────────────────────────────', "green"))

        print(colored(f"Номер телефона в 3-ей базе не найден :( ", "red"))
    except:
        print(colored('База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))

##########################################################################################################
def gemotest (phone):
    try:
        with open('src//gemotest.csv', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split('	')  
                if len(data) >= 27 and data[6] == phone:
                    if main.data['base_out'] == 'S':
                        print(colored('┌──────────────────────────────────────────────────────', "green"))
                        print(colored('│Найдено в базе gemotest', "green"))
                        print(colored('├──────────────────────────────────────────────────────', "green"))
                        print(colored('├id: ' + data[0].strip(), "green"))
                        print(colored('├last_name: ' + data[1].strip(), "green"))
                        print(colored('├first_name: ' + data[2].strip(), "green"))
                        print(colored('├middle_name: ' + data[3].strip(), "green"))
                        print(colored('├birth_date: ' + data[4].strip(), "green"))
                        print(colored('├sex: ' + data[5].strip(), "green"))
                        print(colored('├mobile_phone: ' + data[6].strip(), "green"))
                        print(colored('├home_phone: ' + data[7].strip(), "green"))
                        print(colored('├mail: ' + data[8].strip(), "green"))
                        print(colored('├send_notify_on_phone: ' + data[9].strip(), "green"))
                        print(colored('├address_city: ' + data[10].strip(), "green"))
                        print(colored('├address_street: ' + data[11].strip(), "green"))
                        print(colored('├insurance_number: ' + data[12].strip(), "green"))
                        print(colored('├insurance_company: ' + data[13].strip(), "green"))
                        print(colored('├birth_certificate: ' + data[14].strip(), "green"))
                        print(colored('├passport_number: ' + data[15].strip(), "green"))
                        print(colored('├passport_issued_by: ' + data[16].strip(), "green"))
                        print(colored('├birthplace: ' + data[17].strip(), "green"))
                        print(colored('├parent_id: ' + data[18].strip(), "green"))
                        print(colored('├parent_id_confirmed_flag: ' + data[19].strip(), "green"))
                        print(colored('├created_at: ' + data[20].strip(), "green"))
                        print(colored('├updated_at: ' + data[21].strip(), "green"))
                        print(colored('├deleted_at: ' + data[22].strip(), "green"))
                        print(colored('├citizenship: ' + data[23].strip(), "green"))
                        print(colored('├actual_region: ' + data[24].strip(), "green"))
                        print(colored('├actual_address: ' + data[25].strip(), "green"))
                        print(colored('├birthissued_by: ' + data[26].strip(), "green"))
                        print(colored('└──────────────────────────────────────────────────────', "green"))
                    
                    elif main.data['base_out'] == 'T':
                        print('\n')
                        tree_gemotest = Tree('Gemotest', style='red')
                        tree_gemotest.add('id', style='cyan').add(str(data[0].strip()), style='yellow')
                        tree_gemotest.add('last_name', style='cyan').add(str(data[1].strip()), style='yellow')
                        tree_gemotest.add('first_name', style='cyan').add(str(data[2].strip()), style='yellow')
                        tree_gemotest.add('middle_name', style='cyan').add(str(data[3].strip()), style='yellow')
                        tree_gemotest.add('birth_date', style='cyan').add(str(data[4].strip()), style='yellow')
                        tree_gemotest.add('sex', style='cyan').add(str(data[5].strip()), style='yellow')
                        tree_gemotest.add('mobile_phone', style='cyan').add(str(data[6].strip()), style='yellow')
                        tree_gemotest.add('home_phone', style='cyan').add(str(data[7].strip()), style='yellow')
                        tree_gemotest.add('mail', style='cyan').add(str(data[8].strip()), style='yellow')
                        tree_gemotest.add('send_notify_on_phone', style='cyan').add(str(data[9].strip()), style='yellow')
                        tree_gemotest.add('address', style='cyan').add('address_city', style='cyan').add(str(data[10].strip()), style='yellow').add('address_street', style='cyan').add(str(data[11].strip()), style='yellow')
                        tree_gemotest.add('insurance_number', style='cyan').add(str(data[12].strip()), style='yellow')
                        tree_gemotest.add('insurance_company', style='cyan').add(str(data[13].strip()), style='yellow')
                        tree_gemotest.add('birth_certificate', style='cyan').add(str(data[14].strip()), style='yellow')
                        tree_gemotest.add('passport_number', style='cyan').add(str(data[15].strip()), style='yellow').add('passport_issued_by', style='cyan').add(str(data[16].strip()), style='yellow')
                        tree_gemotest.add('birthplace', style='cyan').add(str(data[17].strip()), style='yellow')
                        tree_gemotest.add('parent_id', style='cyan').add(str(data[18].strip()), style='yellow')
                        tree_gemotest.add('parent_id_confirmed_flag', style='cyan').add(str(data[19].strip()), style='yellow')
                        tree_gemotest.add('created_at', style='cyan').add(str(data[20].strip()), style='yellow')
                        tree_gemotest.add('updated_at', style='cyan').add(str(data[21].strip()), style='yellow')
                        tree_gemotest.add('deleted_at', style='cyan').add(str(data[22].strip()), style='yellow')
                        tree_gemotest.add('citizenship', style='cyan').add(str(data[23].strip()), style='yellow')
                        tree_gemotest.add('actual_region', style='cyan').add(str(data[24].strip()), style='yellow')
                        tree_gemotest.add('actual_address', style='cyan').add(str(data[25].strip()), style='yellow')
                        tree_gemotest.add('birthissued_by', style='cyan').add(str(data[26].strip()), style='yellow')

                    FnFnMn = str(data[1].strip()), str(data[2].strip()), str(data[2].strip())
                    phone_number = str(data[6].strip())
                    birth_date = str(data[4].strip())
                    adres = str(data[10].strip()), str(data[11].strip())
                    mail = str(data[8].strip())
                    passaport_num = str(data[15].strip())
                    passport_issued_by = str(data[16].strip())

                    table.add_row('', '', '', '', '', '', '', '')
                    table.add_row('gemotest', str(FnFnMn), str(phone_number), str(birth_date), str(adres), str(mail), str(passaport_num), str(passport_issued_by))

                    rprint(tree_gemotest)
        print(colored(f"Номер телефона в 4-oй базе не найден :( ", "red"))
    except:
        print(colored('База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))

##########################################################################################################


def start_serch():
    phone = input(Center.XCenter(colored("[+]Введите номер телефона для поиска(без +): ", "cyan")))
    
    tele2_1_06_22(phone)
    zdravcity_1_01_23(phone)
    DNSS_1_09_2022(phone)
    gemotest(phone)

    console = Console()
    console.print(table)




    
