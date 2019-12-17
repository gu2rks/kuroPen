#!/usr/local/bin/python3
import sys, os, time, random, threading, subprocess
from colorama import Fore
from scapy.all import* #scapy

devices = set()
ch = 0
# change ch of interface each 1 sec
def channel_hopper(interface):
    while True:
        ch = random.randint(1, 13) # pick random ch 1-13
        os.system('iw dev %s set channel %d' % (interface, ch))
        print('------------------------------------')
        print('jump to channel: %d' %ch)
        print('------------------------------------')
        time.sleep(2)

def PacketHandler(pkt) :
    # looking for Beacon or ProbeResp
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        if pkt.addr2 not in devices:
            if(str(pkt[Dot11Elt].info) == "b\'\'"):
                print('SSID: %s  BSSID: %s ' % ('HIDDEN', pkt.addr3))
            else:
                bssid = str(pkt[Dot11Elt].info)
                print('SSID: %s  BSSID: %s ' % (bssid[2:(len(bssid) - 1)], pkt.addr3))
            devices.add(pkt.addr3)
def checkInterface(interface):
    run = 'iwconfig {} | grep Mode'.format(interface)
    output = subprocess.Popen(run, shell=True)
    if ('No such device' not in str(output)):
        print(Fore.RED)
        sys.exit()


if __name__ == '__main__':
    # check interface
    checkInterface(sys.argv[1])
    #thread for ch hop
    hopper = threading.Thread(target=channel_hopper, args=(sys.argv[1],))
    hopper.daemon = True
    hopper.start()
    # sniff packet
    sniff(iface = sys.argv[1], count= int( sys.argv[2]), prn = PacketHandler)