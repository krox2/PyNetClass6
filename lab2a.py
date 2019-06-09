import pyeapi
from getpass import getpass
from pprint import pprint
from yaml import load

device_file = open('MyYAML.yaml', 'r')
device_dict = load(device_file)


connection = pyeapi.client.connect(**device_dict, password=getpass())
device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")
#pprint(output)

for ARP_dict in output[0]['result']['ipV4Neighbors']:
    print("{} : {} - seen on {}".format(ARP_dict['hwAddress'],ARP_dict['address'],ARP_dict['interface']))

'''
output = node.enable('show ip arp')
pprint(output)

pprint(output[0]['result']['ipV4Neighbors'])


[{'command': 'show ip arp',
  'encoding': 'json',
  'result': {'dynamicEntries': 4,
             'ipV4Neighbors': [{'address': '10.220.88.1',
'''
