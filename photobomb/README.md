# Photobomb

## IP = 10.10.11.182

## Nmap

### Initial
```
Starting Nmap 7.92 ( https://nmap.org ) at 2023-01-20 06:13 EST                                                                                                                                                                            
Nmap scan report for photobomb.htb (10.10.11.182)                                                                                                                                                                                          
Host is up (0.055s latency).                                                                                                                                                                                                               
Not shown: 998 closed tcp ports (conn-refused)                                                                                                                                                                                             
PORT   STATE SERVICE VERSION                                                                                                                                                                                                               
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e2:24:73:bb:fb:df:5c:b5:20:b6:68:76:74:8a:b5:8d (RSA)
|   256 04:e3:ac:6e:18:4e:1b:7e:ff:ac:4f:e3:9d:d2:1b:ae (ECDSA)
|_  256 20:e0:5d:8c:ba:71:f0:8c:3a:18:19:f2:40:11:d2:9e (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Photobomb
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.97 seconds
```

## Sinatra as WebServer
```html
<h2>Sinatra doesn’t know this ditty.</h2>
  <img src='http://127.0.0.1:4567/__sinatra__/404.png'>
  <div id="c">
    Try this:
    <pre>get &#x27;&#x2F;mlk&#x27; do
  &quot;Hello World&quot;
end
</pre>
  </div>
```