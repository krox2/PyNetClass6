from yaml import load

def readYAML(filename):
    file1 = open(filename, 'r')
    return load(file1)
    raise ValueError("reading file failed")

def printARP(ARP_output):
    for ARP_dict in  ARP_output[0]['result']['ipV4Neighbors']:
        print("{} : {} - seen on {}".format(ARP_dict['hwAddress'],ARP_dict['address'],ARP_dict['interface']))

def print_route(route_output):
    for route, route_dict in route_output[0]['result']['vrfs']['default']['routes'].items():
        if route_dict['routeType'] == 'static':
            print('{} {} next hop is {}'.format(route, route_dict['routeType'], route_dict['vias'][0]['nexthopAddr']))
        if route_dict['routeType'] == 'connected':
            print('{} {}'.format(route, route_dict['routeType']))

'''
output[0]['result']['vrfs']['default']['routes'])
{'0.0.0.0/0': {'directlyConnected': False,
               'hardwareProgrammed': True,
               'kernelProgrammed': True,
               'metric': 0,
               'preference': 1,
               'routeAction': 'forward',
               'routeType': 'static',
               'vias': [{'interface': 'Vlan1', 'nexthopAddr': '10.220.88.1'}]},
 '10.220.88.0/24': {'directlyConnected': True,
                    'hardwareProgrammed': True,
                    'kernelProgrammed': True,
                    'routeAction': 'forward',
                    'routeType': 'connected',
                    'vias': [{'interface': 'Vlan1'}]}}    
print(route_output)
'''
