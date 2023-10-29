import os 
#import sys
import pickle
import baners
import main
import webbrowser
from pathlib import Path

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
    from rich import print as rprint
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.tree import Tree
except:
    os.system('pip install rich')
    from rich import print as rprint
    from rich.layout import Layout
    from rich.tree import Tree

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




def start_serch_telegram():
    import serch_telegram
    print(Center.XCenter(colored(baners.telegram_logo, "cyan")))
    uid = input(Center.XCenter(colored("[+]Введите user_name пользователя: ", "cyan")))

    serch_telegram.find_phone_by_uid_1(uid)
    serch_telegram.find_phone_by_uid_2(uid)
    serch_telegram.find_phone_by_uid_3(uid)