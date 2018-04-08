#!/usr/bin/env bash

if [ id -u -ne 0 ]; then
    echo "This script should be executed with ROOT privilege"
    exit 1
fi

apt update
apt install -y python-pip python-influxdb
pip install -r ./requirements.txt