# Nmap:
to read [link](https://docs.google.com/document/d/1q0FziVZM3zCWhcgtPpljVPzkBX0fMAh6ebrXVM5rg08/edit)
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
kali@kali:~$ ls /usr/share/wordlists/dirbuster/
apache-user-enum-1.0.txt                 directory-list-2.3-medium.txt
apache-user-enum-2.0.txt                 directory-list-2.3-small.txt
directories.jbrofuzz                     directory-list-lowercase-2.3-medium.txt
directory-list-1.0.txt                   directory-list-lowercase-2.3-small.txt
kali@kali:~$ cat /usr/share/wordlists/dirbuster/directory-list-1.0.txt | wc -l
141708
kali@kali:~$ cat /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3- | wc -l
cat: /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-: No such file or directory
0
kali@kali:~$ cat /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt | wc -l
81643
kali@kali:~$ cat /usr/share/wordlists/dirbuster/apache-user-enum-1.0.txt | wc -l
8930
kali@kali:~$ cat /usr/share/wordlists/dirbuster/apache-user-enum-2.0.txt | wc -l
10355
$dirbuster&
```