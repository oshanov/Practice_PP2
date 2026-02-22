import json

with open('sample-data.json','r') as file:
    data = json.load(file)

print('''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')

for i in data['imdata']:
    some = i["l1PhysIf"]["attributes"]

    dn = some['dn']
    descr = some['descr']
    speed = some['speed']
    mtu = some['mtu']

    print(f'{dn:50} {descr:21} {speed:8} {mtu:7}')
