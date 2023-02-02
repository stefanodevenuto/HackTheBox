#!/bin/sh

cd $(dirname $(readlink -f "$0"))
ruby server.rb >>log/photobomb.log 2>&1
