import socket
from termcolor import colored

def port_scan():
    ip = input(colored('[+]введите ip для скана портов: ', "red"))
    count_port = int(input(colored('[+]Ввелиье количество портов для скана: ', "red")))

    def chek_port(ip, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if client.connect_ex((ip, port)):
            pass
        else:
            print(f"Порт {port} открыт!")


    for i in range(count_port):
        chek_port(ip, i)
    