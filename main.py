from scapy.all import *
from scapy.all import *
from scapy.layers.inet import TCP
from scapy.layers.inet6 import IPv6, ICMPv6ND_NS, ICMPv6ND_NA


def packet_callback(packet):
    # Check if it's a Neighbor Discovery Request (ND)
    if IPv6 in packet and ICMPv6ND_NS in packet:
        print("Neighbor Discovery Request:")
        print(packet.summary())

    # Check if it's a Neighbor Discovery Response (NA)
    elif IPv6 in packet and ICMPv6ND_NA in packet:
        print("Neighbor Discovery Response:")
        print(packet.summary())

    # Check if it's Web Communication Sending Data (TCP)
    elif TCP in packet and packet[TCP].sport == 443:  # HTTPS
        print("Web Communication (Sending Data):")
        print(packet.summary())

    # Check if it's Web Communication Receiving Data (TCP)
    elif TCP in packet and packet[TCP].dport == 443:  # HTTPS
        print("Web Communication (Receiving Data):")
        print(packet.summary())


# Capture packets on a specific network interface (e.g., 'Ethernet 4' on Windows)
sniff(iface='Ethernet 4', prn=packet_callback)
