from tabulate import tabulate
from util.create_util import create_devices

# -------------main program---------------
if __name__ == "__main__":
    devices = create_devices(num_devices=20, num_subnets=4)
    print("\n", tabulate(devices, headers="keys"))