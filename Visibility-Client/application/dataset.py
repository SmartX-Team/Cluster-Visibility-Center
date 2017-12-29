from influxdb import InfluxDBClient
# import GeoIP
import random

client = InfluxDBClient('210.125.84.140', 8086, 'root', 'root', 'iovisor')
# gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

f = open("./dataset.txt", 'r')
lines = f.readlines()

# Command and port dataset
comm_list = ['Socket Thread:4430', 'java:1098', 'ssh:22', 'http:80',
    'https:443', 'update-manager:1058', 'gvfsd-http:80', 'unity-scope-home:831',
    'check-new-release:217', 'git-remote-http:80', 'curl:443',
    'ovs-vsswitchd:6633', 'snapd:2243', 'telnet:107', 'wget:80', 'dns-query:53',
    'pop3:110']
comm_weight = [80, 14, 6, 13, 12, 2, 4, 3, 2, 5, 6, 2, 2, 6, 10, 3, 2]
comms = []
for i in range(len(comm_weight)):
    for j in range(comm_weight[i]):
        comms.append(comm_list[i])


# Box internal Ip dataset
box_internal = ['192.168.0.10', '192.168.0.20', '192.168.0.30','192.168.0.40',
'192.168.0.50', '127.0.0.1']
box_internal_weight = [7, 10, 8, 5, 1, 1]
box_internals = []
for i in range(len(box_internal_weight)):
    for j in range(box_internal_weight[i]):
        box_internals.append(box_internal[i])

# Box interConnect Ip dataset
box_interconnect = box_internal + ['210.125.84.130', '210.125.84.131', '210.125.84.132']
box_interconnect_weight = box_internal_weight + [9, 10, 6]
box_interconnects = []
for i in range(len(box_interconnect_weight)):
    for j in range(box_interconnect_weight[i]):
        box_interconnects.append(box_interconnect[i])

# Box external Ip dataset
box_external = box_interconnects + [line[:line.find(':')] for line in lines]

def create_data(ipfool):
    source_addr = random.choice(ipfool)
    destination_addr = random.choice(ipfool)
    comm_and_port = random.choice(comms)
    comm = comm_and_port[:comm_and_port.find(':')]
    port = comm_and_port[comm_and_port.find(':'):]

    json_body = [
        {
            "measurement": "tcp4connect",
            "tags": {
                "comm": comm,
                "source_addr": source_addr,
                "sourcecode": 'KR',
                "destination_addr": destination_addr,
                "destination_port": port,
                # "COUNTRY": gi.country_code_by_addr(destination_addr),
            },
            "fields": {
    	       "PID": random.randint(random.randint(1700, 1800),
                    random.randint(1800, 1900))
            }
        }
    ]
    client.write_points(json_body)

for i in range(200):
    create_data(box_external)

f.close()
