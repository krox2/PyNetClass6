import pyeapi
from getpass import getpass
from pprint import pprint
from my_funcs import readYAML, printARP, print_route
import ipdb

def main():
    devices = readYAML('arista_devices.yaml')
    password = getpass()
#    ipdb.set_trace()
    for name, device_dict in devices.items():
        connection = pyeapi.client.connect(**device_dict, password=password)
        device = pyeapi.client.Node(connection)
        
        output = device.enable("show ip route")
        print()
        print_route(output)
        print()
        
    
if __name__ == "__main__":
    main()
