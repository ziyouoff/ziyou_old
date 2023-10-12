from termcolor import colored
import time

def tele2_1_06_22(phone):
    with open('src//Tele2.ru (06.2022).csv', 'r', encoding='utf-8') as file:        
        for line in file:
            #print(line)
            data = line.strip().split(';')  
            if len(data) >= 3 and data[2] == phone:
                print(colored('┌──────────────────────────────────────────────────────', "green"))
                print(colored('│Найдено в базе Tele2(06.2022)', "green"))
                print(colored('├──────────────────────────────────────────────────────', "green"))
                print(colored('├Почта: ' + data[0].strip(), "green"))
                print(colored('├ФИО: ' + data[1].strip(), "green"))
                print(colored('├Номер Телефона: ' + data[2].strip(), "green"))
                print(colored('└──────────────────────────────────────────────────────', "green"))
            
    print(colored(f"Номер телефона в 1-ой базе не найден :( ", "red"))
##########################################################################################################
def zdravcity_1_01_23(phone):
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
##########################################################################################################
def DNSS_1_09_2022 (phone):
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
##########################################################################################################
def gemotest (phone):
    with open('src//gemotest.csv', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split('	')  
            if len(data) >= 27 and data[6] == phone:
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
##########################################################################################################







    
