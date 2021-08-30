from util.create_util import create_devices
from operator import itemgetter
from tabulate import tabulate
from datetime import datetime
from time import sleep
from random import choice
import nmap

devices = create_devices(25)

print("\n\nusing print")
print(devices)