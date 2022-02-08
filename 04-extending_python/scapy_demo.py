# https://scapy.net/
from scapy.all import *

ip_layer = IP(dst="247ctf.com")
icmp_layer = ICMP()
packet = ip_layer / icmp_layer
r = send(packet)

print(packet.show())

###
# open wireshark directly via scapy:
# wireshark(packet)

# arp scan the local network
# ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") /
#                  ARP(pdst="192.168.10.0/24", timeout=3, verbose=False))

# for item in ans:
#     # print(item)
#     print(item[1].prsc)

###
# scan ports
# SYN = 0x02
# RST = 0x04
# ACK = 0x10

# for port in [22, 80, 139, 443, 445, 8080]:
#     tcp_connect = sr1(IP(dst="127.0.0.1") / TCP(sport=RandShort(),
#                       dport=port, flags="S"), timeout=1, verbose=False)
#     if tcp_connect and tcp_connect.haslayer(TCP):
#         response_flags = tcp_connect.getlayer(TCP).flags
#         print(response_flags)
#         if response_flags == (SYN + ACK):
#             snd_rst = send(IP(dst="127.0.0.1")/TCP(sport(RandShort(), dport=port, flags="AR"), verbose=False))
#             print("{} is open!".format(port))
#         elif response_flags == (RST + ACK):
#             print("{} is closed!".format(port))
#     else:
#         print("{} is closed!".format(port))

### sniff live packets
from scapy.layers.http import HTTPRequest


def process(packet):
    if packet.haslayer(HTTPRequest):
        print(packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode())


# sniff(filter="port 80", prn=process, store=False)

### or examine packet captures
# scapy_cap = rdpcap("error_reporting.pcap")
# for packet in scapy_cap:
#     if packet.getlayer(ICMP):
#         print(packet.load)
#         input()
