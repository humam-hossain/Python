from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()

# for loop to create large number of devices
for index in range(10):
    
    # create device dictionary
    device = dict()

    # random device name
    device["name"] = (
        choice(["r2","r3","r4","r5"])
        + choice(["L","U"])
        + choice(string.ascii_letters)
    )

    # random vendor from choice of cisco, junipar, arista
    device["vendor"] = choice(["cisco", "juniper", "arista"])

    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).84", "14.07X", "8.12(S).810", "28.45"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.83"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.81"])
    device["ip"] = "10.0.0." + str(index)

    # nicely formatted print of one device
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # add this device to list of devices
    devices.append(device)

# use pprint to print data as-is
print("\n_______pprint___________________")
pprint(devices)

# use tabulate to print table of devices
print("\n_________tabular format____________")
print(tabulate(sorted(devices, key=itemgetter("vendor","os","version")), headers="keys"))