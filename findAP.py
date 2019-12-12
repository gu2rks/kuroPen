#!/usr/local/bin/python3
import sys, os, time, random, threading
from scapy.all import*

devices = set()

# change ch of interface each 1 sec
def channel_hopper(interface):
    while True:
        ch = random.randint(1, 13) # pick random ch 1-13
        os.system('iw dev %s set channel %d' % (interface, ch))
        print('jump to channel: %d' %ch)
        time.sleep(2)

def PacketHandler(pkt) :
    # looking for Beacon or ProbeResp
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        if pkt.addr2 not in devices:
            if(str(pkt[Dot11Elt].info) == "b\'\'"):
                print("HIDDEN : "+pkt.addr3)
            else:
                print(str(pkt[Dot11Elt].info) +" : "+pkt.addr3)
            devices.add(pkt.addr3)


if __name__ == '__main__':

    #thread for ch hop
    hopper = threading.Thread(target=channel_hopper, args=(sys.argv[1],))
    hopper.daemon = True
    hopper.start()
    # sniff packet
    sniff(iface = sys.argv[1], count= int( sys.argv[2]), prn = PacketHandler)