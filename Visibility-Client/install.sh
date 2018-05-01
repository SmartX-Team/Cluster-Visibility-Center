#!/usr/bin/env bash

upgrade_kernel(){
    uname -r | grep "4.15"
    if [ $? -eq 0 ]; then
        echo "Kernel was already upgraded to version 4.15"
        return 0
    fi

    wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15.18/linux-headers-4.15.18-041518-generic_4.15.18-041518.201804190330_amd64.deb
    wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15.18/linux-headers-4.15.18-041518_4.15.18-041518.201804190330_all.deb
    wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15.18/linux-image-4.15.18-041518-generic_4.15.18-041518.201804190330_amd64.deb

    dpkg -i *.deb
    rm *.deb
    reboot
}
install_default_packages(){
    apt update
    apt install -y python python-pip
}

install_python_library(){
    add-apt-repository -y ppa:maxmind/ppa
    apt update
    apt install libgeoip1 libgeoip-dev geoip-bin
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

if [ `id -u` -ne 0 ]; then
    echo "This script should be executed with ROOT privilege"
    exit 1;
fi

upgrade_kernel
install_default_packages
install_python_library
install_iovisor