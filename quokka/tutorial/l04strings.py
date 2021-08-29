from pprint import pprint

device1_str = "  r3-L-n7,  cisco,  catalyst 2960,  ios"

# split
print("string strip, split, replace")
device1 = device1_str.split(",")
print("device1 using split:")
print("      ", device1)

# strip
device1 = device1_str.strip().split(",")
print("device1 using strip and split:")
print("      ", device1)

# remove blanks
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n      ", device1)

# remove blanks, change comma to colon
device1_str_colon = device1_str.replace(" ","").replace(",",":")
print("device1 replaced blanks, comma to colon:\n       ", device1_str_colon) 

# loop with strip and split
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item:\n     ", device1)

# strip and split, single line using list comprehension
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using list comprehension:\n     ", device1)

# ignoring case
print("\n\nignoring case")
model = "CSR1000V"
if model == "csr1000v":
    print(f"matched: {model}")
else:
    print(f"didn't match: {model}")

# considering cases
if model.lower() == "csr1000v":
    print(f"matched using lower(): {model}")
else:
    print(f"didn't match: {model}")

# finding substring
print("\n\nfinding subtring")
version = "Virtual XE Software (X86_64_Linux_IOSD-UNIVERSALK9-M), Version 16.11.1a RELEASE SOFTWARE (fc1)"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)

if index >= 0:
    print(f"found version: {expected_version} at location {index}")
else:
    print(f"not found: {expected_version}")

# separating string components
print("\n\nseperating version string components")
version_info = version.split(",")
for part_no, version_info_part in enumerate(version_info):
    print(f"version part {part_no}: {version_info_part.strip()}")
