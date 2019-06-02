import pyeapi
import requests
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
import ipdb
from getpass import getpass

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ipdb.set_trace()

http_headers = {"Content-Type": "application/json-rpc;"}
host = "arista3.lasthop.io"
port = 443
username = "pyclass"
password = getpass()
url = "https://{}:{}/command-api".format(host, port)

json_payload = {
                "jsonrpc": "2.0",
                "method": "runCmds",
                "params": {"version": 1, "cmds": ["show ip arp"], "format": "json"},
                "id": "1",
}

json_data = json.dumps(json_payload)
http_headers["Content-length"] = str(len(json_data))

response = requests.post(
    url,
    headers=http_headers,
    auth=(username, password),
    data=json_data,
    verify=False
)

response = response.json()


print()
pprint(response)
print()

'''
node = pyeapi.connect_to('arista3')

output = node.enable('show ip arp')
pprint(output)

pprint(output[0]['result']['ipV4Neighbors'])


[{'command': 'show ip arp',
  'encoding': 'json',
  'result': {'dynamicEntries': 4,
             'ipV4Neighbors': [{'address': '10.220.88.1',
'''
