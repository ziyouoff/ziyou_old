import os
import main
import nmap as nm
from main import uclear
from rich.console import Console
from rich import print as rprint
from termcolor import colored
from pystyle import Center
from rich.console import Console
from rich.table import Table
from rich.spinner import Spinner

from pystyle import Center
try:
    import socket
except:
    os.system('pip install socket')

#############################################################
#############################################################
#############################################################

table = Table(title="PORTS")
table.add_column("port", style="cyan", no_wrap=True)
table.add_column("name", style="magenta")
table.add_column("status", justify="right", style="yellow")

ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
    115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
    179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
    514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
    995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
    3268: "LDAP", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin", 
    666: 'DooM'}


def port_scan():
    console = Console()
    def chek_port(ip, port):
        try: port_name = ports[port]
        except:port_name = 'NN'

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if client.connect_ex((ip, port)):
            table.add_row(str(port), port_name, "⛔close")

        else:
            table.add_row(str(port), port_name, "✅open")

    ip = input(Center.XCenter(colored('[+]Введите ip для скана портов: ', "red")))
    count_port = [int(count_port) for count_port in input(Center.XCenter(colored('[+]Ввелиье количество портов для скана: ', "red"))).split(', ')]
    print(count_port)

    
    for i in count_port:
        chek_port(ip, i)
        uclear()
        print('\n\n\n\n\n\n\n\n')
        console.print('ip: ' + str(ip) + '       ports: ' + str(count_port), justify="center", style="red")
        console.print(table, justify='center')
    

#############################################################
#############################################################
#############################################################


def wifi_scan():
    print(Center.XCenter(colored('╔═══════════════════════╗', "cyan")))
    print(Center.XCenter(colored('║Введите ip роутера     ║', "cyan")))
    print(Center.XCenter(colored('╠═══════════════════════╣', "cyan")))
    print(Center.XCenter(colored('║[1] - 192.168.0.1      ║', "cyan")))
    print(Center.XCenter(colored('║[2] - 192.168.1.1      ║', "cyan")))
    print(Center.XCenter(colored('║[3] - Свое             ║', "cyan")))
    print(Center.XCenter(colored('╚═══════════════════════╝', "cyan")))
    sekect_rout_ip = input(Center.XCenter(colored("""\n[+]Select> """, "cyan")))
    if sekect_rout_ip == '1':
        wifi_scan()
    elif sekect_rout_ip == '2':
        wifi_scan()
    elif sekect_rout_ip == '3':
        print(colored('Введите ip роутера', "blue"))
        sekect_other_rout_ip = input(colored("""\n[+]> """, "red"))
        wifi_scan(sekect_other_rout_ip)


#############################################################
#############################################################
#############################################################


def snifer():
    os.system('sudo python snifer.py')

#############################################################
#############################################################
#############################################################

def arp_request():
    import scapy.all as scapy

    console = Console()
    arp_table = Table(title="ARP request")
    arp_table.add_column("port", style="cyan", no_wrap=True)
    arp_table.add_column("name", style="magenta")

    os.system('ifconfig')

    def scan(ip):
        arp = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp
        answered_list, ununswered_list = scapy.srp(arp_request_broadcast, timeout=2)

        for element in answered_list:
            table.add_row(str(element[1].psrc), str(element[1].hwsrc))
            uclear()
            console.print('ip: ' + str(ip))
            console.print(table, justify='center')

            #print(element[1].psrc)
            #print(element[1].hwsrc)
            #print('====================================================')

    ip = input(Center.XCenter(colored('Введите локальный ip сети: ', "red")))
    scan(ip)

#############################################################
#############################################################
#############################################################


def main():
    console = Console()
    
 
    console.print('╔════════════════════════════════╗', justify='center', style='yellow')
    console.print('║              ZiMap             ║', justify='center', style='yellow')
    console.print('╠════════════════════════════════╣', justify='center', style='yellow')
    console.print('║ [1] - Сканер портов            ║', justify='center', style='yellow')
    console.print('║ [2] - Просканировать WiFi сеть ║', justify='center', style='yellow')
    console.print('║ [3] - Snifer                   ║', justify='center', style='yellow')
    console.print('║ [4] - ARP запрос               ║', justify='center', style='yellow')
    console.print('║                                ║', justify='center', style='yellow')
    console.print('║ (b) - Вернутся                 ║', justify='center', style='yellow')
    console.print('╚════════════════════════════════╝', justify='center', style='yellow')
    

    select = input(Center.XCenter(colored("""\n[+]Select> """, "red")))

    if select == 'b':
        import main
        main.main_menu()

    elif select == '1':
        port_scan()

    elif select == '2':
        wifi_scan()

    elif select == '3':
        snifer()

    elif select == '4':
        arp_request()

main()