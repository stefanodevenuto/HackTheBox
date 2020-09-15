#!/bin/bash

python -c 'import pty; pty.spawn("/bin/bash")'
 Ctrl-Z
stty raw -echo


