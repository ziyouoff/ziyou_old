import os

from pystyle import Center
try:
    import socket
except:
    os.system('pip install socket')

from termcolor import colored
from pystyle import Center

try:
    from rich.console import Console
    from rich.table import Table
except:
    os.system('pip install Rich')
    from rich.console import Console
    from rich.table import Table

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

def chek_port(ip, port):
        try: port_name = ports[port]
        except:port_name = 'NN'

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if client.connect_ex((ip, port)):
            #print(Center.XCenter(colored(f"[!]Порт [{port} - {port_name}] закрыт", "green")))
            table.add_row(str(port), port_name, "⛔close")
        else:
            #print(Center.XCenter(colored(f"[!]Порт {port} открыт", "red")))
            table.add_row(str(port), port_name, "✅open")


def port_scan():
    ip = input(Center.XCenter(colored('[+]Введите ip для скана портов: ', "red")))
    count_port = [int(count_port) for count_port in input(Center.XCenter(colored('[+]Ввелиье количество портов для скана: ', "red"))).split(', ')]
    print(count_port)

    for i in count_port:
        chek_port(ip, i)

    console = Console()
    console.print(table, justify='center')



def wifi_scan(ip):
    try:
        print(colored('nmap ' + str(ip) + '/24', "grey"))
        os.system('nmap -sn ' + str(ip) + '/24')
        
    except:
        os.system('apt install nmap')



def main():
    print(Center.XCenter(colored('╔═══════════════════════════════╗', "cyan")))
    print(Center.XCenter(colored('║        Cканер портов          ║', "cyan")))
    print(Center.XCenter(colored('╠═══════════════════════════════╣', "cyan")))
    print(Center.XCenter(colored('║[1] - Сканер портов            ║', "cyan")))
    print(Center.XCenter(colored('║[2] - Просканировать WiFi сеть ║', "cyan")))
    print(Center.XCenter(colored('║[b] - Вернутся                 ║', "cyan")))
    print(Center.XCenter(colored('╚═══════════════════════════════╝', "cyan")))
    select = input(Center.XCenter(colored("""\n[+]Select> """, "red")))

    if select == 'b':
        import main
        main.main_menu()

    elif select == '1':
        port_scan()

    elif select == '2':
        print(Center.XCenter(colored('╔═══════════════════════╗', "cyan")))
        print(Center.XCenter(colored('║Введите ip роутера     ║', "cyan")))
        print(Center.XCenter(colored('╠═══════════════════════╣', "cyan")))
        print(Center.XCenter(colored('║[1] - 192.168.0.1      ║', "cyan")))
        print(Center.XCenter(colored('║[2] - 192.168.1.1      ║', "cyan")))
        print(Center.XCenter(colored('║[3] - Свое             ║', "cyan")))
        print(Center.XCenter(colored('╚═══════════════════════╝', "cyan")))

        sekect_rout_ip = input(Center.XCenter(colored("""\n[+]Select> """, "cyan")))
        if sekect_rout_ip == '1':
            wifi_scan('192.168.0.1')
        elif sekect_rout_ip == '2':
            wifi_scan('192.168.1.1')
        elif sekect_rout_ip == '3':
            print(colored('Введите ip роутера', "blue"))
            sekect_other_rout_ip = input(colored("""\n[+]> """, "red"))
            wifi_scan(sekect_other_rout_ip)

    