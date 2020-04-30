# Nmap:
scanning network
```console
$nmap -sn [iprange] #ping scanning, get MAC and IP for every stations
$nmap -sS -F [iprange] #scan open port + fast mode
$nmap -T4 -p- -A [ip]
$#T4 is the speed of scanning, fast=can be detect, slow = slow result
$#-p- is scann all port, cal also do -p [port] if you want to scan specific port.
$#if -p is not given, Nmap will scan only most common port (top 10000)
$#-A got all infomation about each port such as, service version, os version etc
```
Important: nmap some time give wrong OS name/version 

# nikto
- HTTP/HTTPS vulnerability scanning tool.
- Should run wafw00f before to check if there is a WAF behind WA
- If WA have good security machanism, it might block my IP
```console
$nikto [ip]  
```
# DirBuster
- brute forcing web app directory
- tool have nice UI + easy to use.
- need to give a wordlist ```usr/share/worldlist/dirbuster```
```console
$dirbuster&
```