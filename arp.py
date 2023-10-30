import scapy.all as scapy

def scan(ip):
    arp = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp
    answered_list, ununswered_list = scapy.srp(arp_request_broadcast, timeout=2)

    client_list = []
    
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    print(client_list)

scan('10.0.2.15/24')

