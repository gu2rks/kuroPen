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
        time.sleep(1)

def PacketHandler(pkt) :
    # looking for Beacon or ProbeResp
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        if pkt.addr2 not in devices:
            channel = subprocess.getoutput('iwlist {} channel | grep Current'.format(sys.argv[1]))
            if(str(pkt[Dot11Elt].info) == "b\'\'"):
                print('SSID: %s  BSSID: %s  %s' % ('HIDDEN', pkt.addr3, channel))
            else:
                bssid = str(pkt[Dot11Elt].info)
                print(Fore.WHITE + 'SSID: %s  BSSID: %s %s' % (bssid[2:(len(bssid) - 1)], pkt.addr3, channel))
            devices.add(pkt.addr3)

def checkInterface(interface):
    output = subprocess.getoutput('iwconfig {} | grep Mode'.format(interface))
    if ('No such device' in str(output)):
        print(Fore.RED + output + '\n[+]Exit the script, use iwconfig to check the interfaces')
        sys.exit()
    elif ('Monitor' not in str(output)):
        anw = input(Fore.RED +'[x] The given interface is not in Monitor mode. put it to Monitor mode? [Y/N]')
        if (anw.lower() == 'y'):
            print('[x] Kill interfering processes')
            os.system('sudo airmon-ng check kill')
            os.system('sudo ip link set %s down' % interface)
            os.system('sudo iw %s set monitor control' % interface)
            os.system('sudo ip link set %s up' % interface)
            print(Fore.GREEN + 'Monitor mode is up')
        else:
            print('cya nextime')
            sys.exit()


if __name__ == '__main__':
    # check interface
    checkInterface(sys.argv[1])
    #thread for ch hop
    hopper = threading.Thread(target=channel_hopper, args=(sys.argv[1],))
    hopper.daemon = True
    hopper.start()
    # sniff packet
    sniff(iface = sys.argv[1], prn = PacketHandler)
    