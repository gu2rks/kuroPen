#!/usr/local/bin/python3
import sys
from scapy.all import*

devices = set()
def PacketHandler(pkt) :
    if pkt.haslayer(Dot11Beacon):
        if pkt.addr2 not in devices:
            print (pkt.addr2)
            devices.add(pkt.addr2)


sniff(iface = sys.argv[1], count= int( sys.argv[2]), prn = PacketHandler)  