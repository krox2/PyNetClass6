import pyeapi
from pprint import pprint

node = pyeapi.connect_to('arista3')

output = node.enable('show ip arp')
pprint(output)

pprint(output[0]['result']['ipV4Neighbors'])

'''
[{'command': 'show ip arp',
  'encoding': 'json',
  'result': {'dynamicEntries': 4,
             'ipV4Neighbors': [{'address': '10.220.88.1',
'''
