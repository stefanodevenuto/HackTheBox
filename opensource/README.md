# RedPanda

## IP = 10.10.11.164

## Nmap

### Initial
```
80/tcp   open     http    Werkzeug/2.1.2 Python/3.10.3                                                                                                                                        
| fingerprint-strings:                                                                                                                                                                                                                      
|   GetRequest:                                                                                                                                                                                                                             
|     HTTP/1.1 200 OK                                                                                                                                                                                                                       
|     Server: Werkzeug/2.1.2 Python/3.10.3                                                                                                                                                                                                  
|     Date: Tue, 09 Aug 2022 08:43:16 GMT                                                                                                                                                                                                   
|     Content-Type: text/html; charset=utf-8                                                                                                                                                                                                
|     Content-Length: 5316                                                                                                                                                                                                                  
|     Connection: close                                                                                                                                                                                                                     
|     <html lang="en">                                                                                                                                                                                                                      
|     <head>                                                                                                                                                                                                                                
|     <meta charset="UTF-8">                                                                                                                                                                                                                
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">                                                                                                                                                                
|     <title>upcloud - Upload files for Free!</title>                                                                                                                                                                                       
|     <script src="/static/vendor/jquery/jquery-3.4.1.min.js"></script>                                                                                                                                                                     
|     <script src="/static/vendor/popper/popper.min.js"></script>                                                                                                                                                                           
|     <script src="/static/vendor/bootstrap/js/bootstrap.min.js"></script>                                                                                                                                                                  
|     <script src="/static/js/ie10-viewport-bug-workaround.js"></script>                                                                                                                                                                    
|     <link rel="stylesheet" href="/static/vendor/bootstrap/css/bootstrap.css"/>                                                                                                                                                            
|     <link rel="stylesheet" href=" /static/vendor/bootstrap/css/bootstrap-grid.css"/>                                                                                                                                                      
|     <link rel="stylesheet" href=" /static/vendor/bootstrap/css/bootstrap-reboot.css"/>                                                                                                                                                    
|     <link rel=                                                                                                                                                                                                                            
|   HTTPOptions:                                                                                                                                                                                                                            
|     HTTP/1.1 200 OK                                                                                                                                                                                                                       
|     Server: Werkzeug/2.1.2 Python/3.10.3                                                                                                                                                                                                  
|     Date: Tue, 09 Aug 2022 08:43:16 GMT                                                                                                                                                                                                   
|     Content-Type: text/html; charset=utf-8                                                                                                                                                                                                
|     Allow: HEAD, OPTIONS, GET                                                                                                                                                                                                             
|     Content-Length: 0                                                                                                                                                                                                                     
|     Connection: close                                                                                                                                                                                                                     
|   RTSPRequest:                                                                                                                                                                                                                            
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"                                                                                                                                                                                     
|     "http://www.w3.org/TR/html4/strict.dtd">                                                                                                                                                                                              
|     <html>                                                                                                                                                                                                                                
|     <head>                                                                                                                                                                                                                                
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">                                                                                                                                                                    
|     <title>Error response</title>                                                                                                                                                                                                         
|     </head>                                                                                                                                                                                                                               
|     <body>                                                                                                                                                                                                                                
|     <h1>Error response</h1>                                                                                                                                                                                                               
|     <p>Error code: 400</p>                                                                                                                                                                                                                
|     <p>Message: Bad request version ('RTSP/1.0').</p>                                                                                                                                                                                     
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>                                                                                                                                     
|     </body>                                                                                                                                                                                                                               
|_    </html>                                                                                                                                                                                                                               
|_http-title: upcloud - Upload files for Free!                                                                                                                                                                                              
|_http-server-header: Werkzeug/2.1.2 Python/3.10.3

3000/tcp filtered ppp
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.92%I=7%D=8/9%Time=62F21DFE%P=x86_64-pc-linux-gnu%r(GetRe
SF:quest,1573,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20Werkzeug/2\.1\.2\x20Py
SF:thon/3\.10\.3\r\nDate:\x20Tue,\x2009\x20Aug\x202022\x2008:43:16\x20GMT\
SF:r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x205
SF:316\r\nConnection:\x20close\r\n\r\n<html\x20lang=\"en\">\n<head>\n\x20\
SF:x20\x20\x20<meta\x20charset=\"UTF-8\">\n\x20\x20\x20\x20<meta\x20name=\
SF:"viewport\"\x20content=\"width=device-width,\x20initial-scale=1\.0\">\n
SF:\x20\x20\x20\x20<title>upcloud\x20-\x20Upload\x20files\x20for\x20Free!<
SF:/title>\n\n\x20\x20\x20\x20<script\x20src=\"/static/vendor/jquery/jquer
SF:y-3\.4\.1\.min\.js\"></script>\n\x20\x20\x20\x20<script\x20src=\"/stati
SF:c/vendor/popper/popper\.min\.js\"></script>\n\n\x20\x20\x20\x20<script\
SF:x20src=\"/static/vendor/bootstrap/js/bootstrap\.min\.js\"></script>\n\x
SF:20\x20\x20\x20<script\x20src=\"/static/js/ie10-viewport-bug-workaround\
SF:.js\"></script>\n\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=
SF:\"/static/vendor/bootstrap/css/bootstrap\.css\"/>\n\x20\x20\x20\x20<lin
SF:k\x20rel=\"stylesheet\"\x20href=\"\x20/static/vendor/bootstrap/css/boot
SF:strap-grid\.css\"/>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20hre
SF:f=\"\x20/static/vendor/bootstrap/css/bootstrap-reboot\.css\"/>\n\n\x20\
SF:x20\x20\x20<link\x20rel=")%r(HTTPOptions,C7,"HTTP/1\.1\x20200\x20OK\r\n
SF:Server:\x20Werkzeug/2\.1\.2\x20Python/3\.10\.3\r\nDate:\x20Tue,\x2009\x
SF:20Aug\x202022\x2008:43:16\x20GMT\r\nContent-Type:\x20text/html;\x20char
SF:set=utf-8\r\nAllow:\x20HEAD,\x20OPTIONS,\x20GET\r\nContent-Length:\x200
SF:\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,1F4,"<!DOCTYPE\x20HTML
SF:\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x2
SF:0\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equi
SF:v=\"Content-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x2
SF:0\x20\x20\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x20
SF:</head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Er
SF:ror\x20response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:
SF:\x20400</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Bad\x20requ
SF:est\x20version\x20\('RTSP/1\.0'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20<p>Error\x20code\x20explanation:\x20HTTPStatus\.BAD_REQUEST\x20-\x20B
SF:ad\x20request\x20syntax\x20or\x20unsupported\x20method\.</p>\n\x20\x20\
SF:x20\x20</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 213.90 seconds
```

### /console
- WERKZEUG Debugger, requires a PIN, can be random or set by the env variable WERKZEUG_DEBUG_PIN
- PIN (max?) length: 14

### /uploads/<not-existing-file>
- SECRET = "0BqI9BxOuJAlUwmxinmI" "0eJhLrr2KrtrkQwfdUKs", it changes
- Probable full path: `/usr/local/lib/python3.10/site-packages/flask/app.py`
- arthur