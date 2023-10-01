import os
try:
    import socket
except:
    os.system('pip install socket')
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



def wifi_scan(ip):
    try:
        print(colored('nmap ' + str(ip) + '/24', "grey"))
        os.system('nmap -sn ' + str(ip) + '/24')
        
    except:
        os.system('apt install nmap')



def main():
    print(colored('[1] - Сканер портов', "blue"))
    print(colored('[2] - Просканировать WiFi сеть', "blue"))
    select = input(colored("""\n[+]> """, "red"))

    if select == '1':
        port_scan()

    elif select == '2':
        print(colored('Введите ip роутера', "blue"))
        print(colored('[1] - 192.168.0.1', "blue"))
        print(colored('[2] - 192.168.1.1', "blue"))
        print(colored('[3] - Свое', "blue"))

        sekect_rout_ip = input(colored("""\n[+]> """, "red"))
        if sekect_rout_ip == '1':
            wifi_scan('192.168.0.1')
        elif sekect_rout_ip == '2':
            wifi_scan('192.168.1.1')
        elif sekect_rout_ip == '3':
            print(colored('Введите ip роутера', "blue"))
            sekect_other_rout_ip = input(colored("""\n[+]> """, "red"))
            wifi_scan(sekect_other_rout_ip)

    