#!/usr/bin/env python

# Usage:
#   $ KEY=<YOUR MASTER API KEY> python example.py

import os
import time

from m2x.client import M2XClient

# Instantiate a client
client = M2XClient(key=os.environ['API_KEY'])

# Create a device
device = client.create_device(
    name='Current Time Example',
    description='Store current time every 10 seconds',
    visibility='public'
)

print device.id