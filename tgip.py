from termcolor import colored
import ipaddress
import netifaces
import requests
import argparse
import platform
import pyshark
import socket
import sys
import os

from port_scan import port_scan

def check_tshark_availability():
    tshark_path = os.popen('which tshark').read().strip()

    if not tshark_path:
        print(colored("[-]TShark Не установлен", "red"))
        install_qv = input('[+]Установить? y/n')
        if install_qv == 'y' or 'Y':
            try:
                print(colored("[+]Установка"))
                os.system('apt install tshark')
            except:
                print(colored('sudo apt install tshark'), 'yellow')
        else:
            print(colored('sudo apt install tshark'), 'yellow')
        
    else:
        print(colored("[+] TShark установлен \n", "green"))


# Telegram AS list of excluded IP ranges
EXCLUDED_NETWORKS = ['91.108.13.0/24', '149.154.160.0/21', '149.154.160.0/22',
                     '149.154.160.0/23', '149.154.162.0/23', '149.154.164.0/22',
                     '149.154.164.0/23', '149.154.166.0/23', '149.154.168.0/22',
                     '149.154.172.0/22', '185.76.151.0/24', '91.105.192.0/23',
                     '91.108.12.0/22', '91.108.16.0/22', '91.108.20.0/22',
                     '91.108.4.0/22', '91.108.56.0/22', '91.108.56.0/23',
                     '91.108.58.0/23', '91.108.8.0/22', '95.161.64.0/20']


def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None


def get_my_ip():
    try:
        return requests.get('https://icanhazip.com').text.strip()
    except Exception as e:
        print(f"[!] Error fetching external IP: {e}")
        return None


def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        hostname = get_hostname(ip)
        if hostname:
            print(f"[+] Hostname: {hostname}")
        return data
    except Exception as e:
        print(f"[!] Error fetching whois data: {e}")
        return None


def display_whois_info(data):
    if not data:
        return

    print(f"[+] Страна: {data.get('country', 'N/A')})")
    print(f"[+] Код страны: {data.get('countryCode', 'N/A')}")
    print(f"[+] Регион: {data.get('region', 'N/A')}")
    print(f"[+] Имя региона: {data.get('regionName', 'N/A')}")
    print(f"[+] Город: {data.get('city', 'N/A')}")
    print(f"[+] Zip Code: {data.get('zip', 'N/A')}")
    print(f"[+] Latitude: {data.get('lat', 'N/A')}")
    print(f"[+] Longitude: {data.get('lon', 'N/A')}")
    print(f"[+] Time Zone: {data.get('timezone', 'N/A')}")
    print(f"[+] ISP: {data.get('isp', 'N/A')}")
    print(f"[+] Organization: {data.get('org', 'N/A')}")
    print(f"[+] AS: {data.get('as', 'N/A')} \n")


def is_excluded_ip(ip):
    for network in EXCLUDED_NETWORKS:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(network):
            return True
    return False


def choose_interface():
    interfaces = netifaces.interfaces()
    print("[+] Доступные интерфейсы:")
    for idx, iface in enumerate(interfaces, 1):
        print(f"{idx}. {iface}")
    choice = int(input("[+]Введите номер сетевого интерефейса (Что бы помотреть все используйте команду ifconfig): "))
    return interfaces[choice - 1]


def extract_stun_xor_mapped_address(interface):
    print("[+] Жду звонка...\n")

    cap = pyshark.LiveCapture(interface=interface, display_filter="stun")
    my_ip = get_my_ip()

    for packet in cap.sniff_continuously(packet_count=250):
        if hasattr(packet, 'ip'):
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst

            if is_excluded_ip(src_ip) or is_excluded_ip(dst_ip):
                continue

            if packet.stun:
                xor_mapped_address = packet.stun.get_field_value('stun.att.ipv4')

                if xor_mapped_address:
                    if xor_mapped_address != my_ip:
                        return xor_mapped_address
    return None


def main():
    try:
        try:
            os.system('python3 -m venv venv')
            os.system('source ./venv/bin/activate')
        except:
            print(colored('[!]', "red"))

        check_tshark_availability()
        interface_name = choose_interface()

        ip_address = extract_stun_xor_mapped_address(interface_name)
        if ip_address:
            print(colored(f"[+] IP: {ip_address} \n", "red"))
            ip_data = get_ip_info(ip_address)
            display_whois_info(ip_data)
            
        else:
            print(colored("[!] Не удалось определить IP-адрес.", "red"))
    except (KeyboardInterrupt, EOFError):
        print("\n[+] Exiting gracefully...")
        pass