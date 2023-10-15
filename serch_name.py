from termcolor import colored

def pasports_1 (FIO):
    try:
        with open('src//pasports_1.csv', 'r', encoding='utf-8') as file:        
            for line in file:
                data = line.strip().split('|')  
                if len(data) >= 8:
                    if FIO.replace(' ', '') in data[0].replace(' ', '') or data[0].replace(' ', '') in FIO.replace(' ', ''):
                        print(colored('┌──────────────────────────────────────────────────────', "green"))
                        print(colored('│Найдено в базе Паспортов(09.2022)', "green"))
                        print(colored('├──────────────────────────────────────────────────────', "green"))
                        print(colored('├' + data[0].strip(), "green"))
                        print(colored('├' + data[1].strip(), "green"))
                        print(colored('├' + data[2].strip(), "green"))
                        print(colored('├' + data[3].strip(), "green"))
                        print(colored('├' + data[4].strip(), "green"))
                        print(colored('├' + data[5].strip(), "green"))
                        print(colored('├' + data[6].strip(), "green"))
                        print(colored('├' + data[7].strip(), "green"))
                        print(colored('├' + data[8].strip(), "green"))
                        print(colored('└──────────────────────────────────────────────────────', "green"))

        print(colored(f"Номер телефона в 1 базе не найден :( ", "red"))
    except:
        print(colored('База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))

def tele2_1_06_22(FIO):
    try:    
        with open('src//Tele2.ru (06.2022).csv', 'r', encoding='utf-8') as file:        
            for line in file:
                data = line.strip().split(';')  
                if len(data) >= 3:
                    if FIO.replace(' ', '') in data[1].replace(' ', '') or data[1].replace(' ', '') in FIO.replace(' ', ''):
                        print(colored('┌──────────────────────────────────────────────────────', "green"))
                        print(colored('│Найдено в базе Tele2(06.2022)', "green"))
                        print(colored('├──────────────────────────────────────────────────────', "green"))
                        print(colored('├Почта: ' + data[0].strip(), "green"))
                        print(colored('├ФИО: ' + data[1].strip(), "green"))
                        print(colored('├Номер Телефона: ' + data[2].strip(), "green"))
                        print(colored('└──────────────────────────────────────────────────────', "green"))

        print(colored(f"Номер телефона вo 2-ой базе не найден :( ", "red"))
    except:
        print(colored(f'База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))


def zdravcity_1_01_23(FIO):
    try:
        with open('src//zdravcity.ru_1_01_2023.csv', 'r', encoding='utf-8') as file:        
            for line in file:
                data = line.strip().split('		')  
                if len(data) >= 8:
                    if FIO.replace(' ', '') in data[2].replace(' ', '') or data[2].replace(' ', '') in FIO.replace(' ', ''):
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

def gemotest (FIO):
    try:
        with open('src//gemotest.csv', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split('	')  
                if len(data) >= 27 and data[1] in FIO:
                    if FIO.replace(' ', '') in data[1].replace(' ', '') or FIO.replace(' ', '') in data[2].replace(' ', '') or FIO.replace(' ', '') in data[3].replace(' ', ''):
                        print(colored('┌──────────────────────────────────────────────────────', "green"))
                        print(colored('│Найдено в базе gemotest', "green"))
                        print(colored('├──────────────────────────────────────────────────────', "green"))
                        print(colored('├id: ' + data[0].strip(), "green"))
                        print(colored('├last name: ' + data[1].strip(), "green"))
                        print(colored('├first name: ' + data[2].strip(), "green"))
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

        print(colored(f"Номер телефона в 4-oй базе не найден :( ", "red"))
    except:
        print(colored('База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))


def ru_base (FIO):
    try:
        with open('src//ru_base.csv', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')  
                if len(data) >= 3 and data[1] in FIO:
                    if FIO.replace(' ', '') in data[1].replace(' ', ''):
                        print(colored('┌──────────────────────────────────────────────────────', "green"))
                        print(colored('│Найдено в базе gemotest', "green"))
                        print(colored('├──────────────────────────────────────────────────────', "green"))
                        print(colored('├ФИО: ' + data[0].strip(), "green"))
                        print(colored('├Дата рождения: ' + data[1].strip(), "green"))
                        print(colored('├Номер телефона: ' + data[2].strip(), "green"))
                        print(colored('├Почта: ' + data[3].strip(), "green"))
                        print(colored('└──────────────────────────────────────────────────────', "green"))

        print(colored(f"Номер телефона в 4-oй базе не найден :( ", "red"))
    except:
        print(colored('База не найдена или произошла иная ошибка, продожаю поиск в других базах', "red"))