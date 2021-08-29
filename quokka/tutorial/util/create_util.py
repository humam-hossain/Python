from random import choice
import string

def create_devices(num_devices=1, num_subnets=1):
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requsted")
        return create_devices
    
    for subnet_index in range(1, num_subnets+1):
        # for loop to create large number of devices
        for device_index in range(1, num_devices+1):
            
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
            device["ip"] = "10.0."+ str(subnet_index) + "." + str(device_index)

            # add this device to list of devices
            created_devices.append(device)
    return created_devices
