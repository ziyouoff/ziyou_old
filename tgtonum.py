from termcolor import colored
import baners
def find_phone_by_uid(uid):
    with open('tg_base_1.txt', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.split('|')
            if data[6].strip() == uid:
                return data[4].strip()
    return None

def tgtonum():
    print(colored(baners.telegram_logo, "cyan"))
    uid = input(colored("Введите UID пользователя: ", "cyan"))
    phone = find_phone_by_uid(uid)
    if phone:
        print(colored(f"Номер телефона для {uid}: {phone}", "green"))
    else:
        print(colored(f"Номер телефона для {uid} не найден :( ).", "red"))