from termcolor import colored
import baners
def find_phone_by_uid_1(uid):
    with open('src//tg_base_1.txt', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.split('|')
            if data[6].strip() == uid:
                print(colored('┌──────────────────────────────────────────────────────', "green"))
                print(colored('│1-ая база из 3', "green"))
                print(colored('├──────────────────────────────────────────────────────', "green"))
                print(colored('├name: ' + data[2].strip(), "green"))
                print(colored('├fname: ' + data[3].strip(), "green"))
                print(colored('├Номер телефона: ' + data[4].strip(), "green"))
                print(colored('├user_id: ' + data[5].strip(), "green"))
                print(colored('├user_name: ' + data[6].strip(), "green"))
                print(colored('└──────────────────────────────────────────────────────', "green"))
    print(colored(f"Номер телефона в 1-ой бфзе не найден :( ", "red"))



def find_phone_by_uid_2(uid):
    with open('src//tg_base_2(YOG).csv', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.split(',')
            if data[2].strip() == uid:
                print(colored('┌──────────────────────────────────────────────────────', "green"))
                print(colored('│2-ая база из 3(Глаз Бога)', "green"))
                print(colored('├──────────────────────────────────────────────────────', "green"))
                print(colored('├id: ' + data[0].strip(), "green"))
                print(colored('├Номер телефона: ' + data[1].strip(), "green"))
                print(colored('├user_name: ' + data[2].strip(), "green"))
                print(colored('├fers_name: ' + data[3].strip(), "green"))
                print(colored('├last_name: ' + data[4].strip(), "green"))
                print(colored('└──────────────────────────────────────────────────────', "green"))

    print(colored(f"Номер телефона во 2-ой базе не найден :( ", "red"))



def find_phone_by_uid_3(uid):
    with open('src//tg_base_3(chelabinsk).csv', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.split(',')
            if data[2].strip() == uid:
                print(colored('┌──────────────────────────────────────────────────────', "green"))
                print(colored('│3-ая база из 3(Челябинск)', "green"))
                print(colored('├──────────────────────────────────────────────────────', "green"))
                print(colored('├id: ' + data[0].strip(), "green"))
                print(colored('├fers_name: ' + data[1].strip(), "green"))
                print(colored('├user_name: ' + data[2].strip(), "green"))
                print(colored('├Номер телефона: ' + data[3].strip(), "green"))
                print(colored('└──────────────────────────────────────────────────────', "green"))

    print(colored(f"Номер телефона в 3-ей базе не найден :( ", "red"))


def tgtonum():
    print(colored(baners.telegram_logo, "cyan"))
    uid = input(colored("[+]Введите user_name пользователя: ", "cyan"))

    find_phone_by_uid_1(uid)
    find_phone_by_uid_2(uid)
    find_phone_by_uid_3(uid)
    