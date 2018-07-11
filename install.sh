#!/usr/bin/env bash

install_python_packages(){
    apt update
    apt install -y python-pip python-influxdb
    pip install -r ./requirements.txt
}

install_influxdb(){
    curl -sL https://repos.influxdata.com/influxdb.key | apt-key add -
    source /etc/lsb-release
    echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | tee /etc/apt/sources.list.d/influxdb.list

    apt-get update
    apt-get -y install influxdb
    service influxdb start
}

install_grafana(){
    echo "deb https://packagecloud.io/grafana/stable/debian/ stretch main" >> /etc/apt/sources.list
    curl https://packagecloud.io/gpg.key | apt-key add -

    apt-get update
    apt-get -y install grafana

    systemctl daemon-reload
    systemctl start grafana-server.service
    systemctl status grafana-server.service

    systemctl enable grafana-server.service
}

install_grafana_plugin(){
    grafana-cli plugins install grafana-worldmap-panel
    systemctl restart grafana-server.service
}
if [ `id -u` -ne 0 ]; then
    echo "This script should be executed with ROOT privilege"
    exit 1
fi

install_python_packages
install_influxdb
install_grafana
install_grafana_plugin