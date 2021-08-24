from pprint import pprint

# dictionary representing a device
device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1"
}

# simple print
print("\n___________SIMPLE PRINT__________________")
print("device: ", device)
print("device name: ", device["name"])

# pretty print
print("\n__________PRETTY PRINT____________________")
pprint(device)

# for loop, nicely formatted print
print("\n_________FOR LOOP, USING F-STRING")
for key, value in device.items():
    print(f"{key:>16s} : {value}")