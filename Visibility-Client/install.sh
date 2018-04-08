#!/usr/bin/env bash

install_default_packages(){
    apt update
    apt install -y python
}

install_python_library(){
    apt install -y python-influxdb
    pip install -r ./requirements.txt
}

install_iovisor(){
    # Only the nightly packages are build for Ubuntu 16.04,
    # but the steps are very straightforward.
    # No need to upgrade the kernel or complile from source!
    echo "deb [trusted=yes] https://repo.iovisor.org/apt/xenial xenial-nightly main" | sudo tee /etc/apt/sources.list.d/iovisor.list
    sudo apt-get update
    sudo apt-get install -y bcc-tools libbcc-examples
}

if [ id -u -ne 0 ]; then
    echo "This script should be executed with ROOT privilege"
    exit 1;
fi

install_default_packages
install_python_library
install_iovisor