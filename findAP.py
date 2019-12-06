#!/usr/local/bin/python3
import sys
from scapy.all import*

devices = set()
def PacketHandler(pkt) :
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        if pkt.addr2 not in devices:
            if(str(pkt[Dot11Elt].info) == "b\'\'"):
                print("HIDDEN : "+pkt.addr3)
            else:
                print(str(pkt[Dot11Elt].info) +" : "+pkt.addr3)
            devices.add(pkt.addr3)


sniff(iface = sys.argv[1], count= int( sys.argv[2]), prn = PacketHandler)  