from util.create_util import create_devices
from operator import itemgetter
from pprint import pprint
from tabulate import tabulate
from datetime import datetime
from time import sleep
from random import choice
import nmap 

devices = create_devices(25)

print("\n\nusing print")
print(devices)

print("\n\nusing pprint")
pprint(devices)

print("\n\nusing loop")
for device in devices:
    sleep(0.1)
    device["last heard"] = str(datetime.now())
    print(device)

print("\n\nusing tabulate")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))

print("\n\nusing loop and f-string")
print("     Name     Vendor : Os      Ip Address      Last Heard")
print("     -----    ------   -----   -----------     -----------------")
for device in devices:
    print(f'{device["name"]:>8s}  {device["vendor"]:>10s} : {device["os"]:<6s}  {device["ip"]:<15s}  {device["last heard"][:-4]}')

print("\nsame thing but sorted by last heard in reverse order")
for device in sorted(devices, key=itemgetter("last heard"), reverse=True):
    print(f'{device["name"]:>8s}  {device["vendor"]:>10s} : {device["os"]:<6s}  {device["ip"]:<15s}  {device["last heard"][:-4]}')


print("\n\nmultiple print statement, same line")
print("testing devices:")
for device in devices:
    print(f'-----tesing device {device["name"]} ------', end="")
    sleep(choice([0.1, 0.2, 0.3, 0.4]))
    print("done.")
print("testing completed")

nm = nmap.PortScanner()

while True:
    ip = input("\nInput ip address to scan: ")
    
    if not ip:
        break

    print(f'--- begining scan of {ip}')
    output = nm.scan(ip, '22-1824')
    print(f'--- --- command: {nm.command_line()}')

    print("nmap scan output")
    pprint(output)