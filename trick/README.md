
# Trick

## IP = 10.10.11.166

## Nmap

### Initial
```
# Nmap 7.92 scan initiated Mon Jul 25 03:23:01 2022 as: nmap -sC -sV -oN nmap/initial 10.10.11.166
Nmap scan report for 10.10.11.166
Host is up (0.059s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:
|   2048 61:ff:29:3b:36:bd:9d:ac:fb:de:1f:56:88:4c:ae:2d (RSA)
|   256 9e:cd:f2:40:61:96:ea:21:a6:ce:26:02:af:75:9a:78 (ECDSA)
|_  256 72:93:f9:11:58:de:34:ad:12:b5:4b:4a:73:64:b9:70 (ED25519)
25/tcp open  smtp    Postfix smtpd
|_smtp-commands: debian.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
53/tcp open  domain  ISC BIND 9.11.5-P4-5.1+deb10u7 (Debian Linux)
| dns-nsid:
|_  bind.version: 9.11.5-P4-5.1+deb10u7-Debian
80/tcp open  http    nginx 1.14.2
|_http-title: Coming Soon - Start Bootstrap Theme
|_http-server-header: nginx/1.14.2
Service Info: Host:  debian.localdomain; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 25 03:23:54 2022 -- 1 IP address (1 host up) scanned in 53.06 seconds
```

### Fullscan
```
# Nmap 7.92 scan initiated Mon Jul 25 03:26:14 2022 as: nmap -sC -p- -sV -oN nmap/fullscan 10.10.11.166
Nmap scan report for 10.10.11.166
Host is up (0.043s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:
|   2048 61:ff:29:3b:36:bd:9d:ac:fb:de:1f:56:88:4c:ae:2d (RSA)
|   256 9e:cd:f2:40:61:96:ea:21:a6:ce:26:02:af:75:9a:78 (ECDSA)
|_  256 72:93:f9:11:58:de:34:ad:12:b5:4b:4a:73:64:b9:70 (ED25519)
25/tcp open  smtp    Postfix smtpd
|_smtp-commands: debian.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
53/tcp open  domain  ISC BIND 9.11.5-P4-5.1+deb10u7 (Debian Linux)
| dns-nsid:
|_  bind.version: 9.11.5-P4-5.1+deb10u7-Debian
80/tcp open  http    nginx 1.14.2
|_http-title: Coming Soon - Start Bootstrap Theme
|_http-server-header: nginx/1.14.2
Service Info: Host:  debian.localdomain; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 25 03:32:15 2022 -- 1 IP address (1 host up) scanned in 360.26 seconds
```

## Gobuster
```
# gobuster dir -u "http://10.10.11.166/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt,html,php,js

===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.166/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/07/25 03:29:15 Starting gobuster in directory enumeration mode
===============================================================
/assets               (Status: 301) [Size: 185] [--> http://10.10.11.166/assets/]
/css                  (Status: 301) [Size: 185] [--> http://10.10.11.166/css/]   
/js                   (Status: 301) [Size: 185] [--> http://10.10.11.166/js/]
/index.html           (Status: 200) [Size: 5480]    
                                                                                 
===============================================================
2022/07/25 03:47:46 Finished
===============================================================
```

## DNS Enumeration

### nslookup
```
> SERVER 10.10.11.166
Default server: 10.10.11.166
Address: 10.10.11.166#53
> 127.0.0.1
1.0.0.127.in-addr.arpa  name = localhost.
> 10.10.14.25
** server can't find 25.14.10.10.in-addr.arpa: NXDOMAIN
> 10.10.11.166
166.11.10.10.in-addr.arpa       name = trick.htb.
```
We can see the domain name __trick.htb__

### dig (look at data in transfer zones)
```
# dig axfr trick.htb @10.10.11.166

; <<>> DiG 9.18.1-1-Debian <<>> axfr trick.htb @10.10.11.166
;; global options: +cmd
trick.htb.              604800  IN      SOA     trick.htb. root.trick.htb. 5 604800 86400 2419200 604800
trick.htb.              604800  IN      NS      trick.htb.
trick.htb.              604800  IN      A       127.0.0.1
trick.htb.              604800  IN      AAAA    ::1
preprod-payroll.trick.htb. 604800 IN    CNAME   trick.htb.
trick.htb.              604800  IN      SOA     trick.htb. root.trick.htb. 5 604800 86400 2419200 604800
;; Query time: 51 msec
;; SERVER: 10.10.11.166#53(10.10.11.166) (TCP)
;; WHEN: Tue Jul 26 09:43:33 EDT 2022
;; XFR size: 6 records (messages 1, bytes 231)
```
We can recover two subdomains: root.trick.htb (same page as trick.htb) and __preprod-payroll.trick.htb__

### In users.php, found username: Enemigosss. By sending request `GET /manage_user.php?id=1` we obtain: Enemigoss:SuperGucciRainbowCake

