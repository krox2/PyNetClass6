import pyeapi
from getpass import getpass
from pprint import pprint
from my_funcs import readYAML, printARP


def main():
    devices = readYAML('arista_devices.yaml')
    password = getpass()
    for name, device_dict in devices.items():
        connection = pyeapi.client.connect(**device_dict, password=password)
        device = pyeapi.client.Node(connection)
        
        output = device.enable("show ip arp")
        print()
        printARP(output)
        print()
    
if __name__ == "__main__":
    main()
