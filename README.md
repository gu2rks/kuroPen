# Requriment
- Kali linux !

# what is this repo?
Just a playgroud for me, who try to learn python + scapy.

Still a NOOB but you will call me **OZAMI** one day...


## mounting shared folder in Kali
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other


## Good link:
* Probe Request/Response: https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/
* Beacon: https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/
* scapy 802.11: https://scapy.readthedocs.io/en/latest/api/scapy.layers.dot11.html

# To do
- [x] jump to different channel
- [x] put interface to monitor mode
- [ ] show AP's channel (check LEShortField in scapy)
- [ ] Dauth attack?