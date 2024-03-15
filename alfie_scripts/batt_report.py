#!/usr/bin/env python3

import subprocess

def get_bluetooth_info():
    # Execute the ioreg command and capture its output for all devices
    result = subprocess.run(['ioreg', '-l'], stdout=subprocess.PIPE, text=True)

    # Print the output to manually search for your device and battery info
    print(result.stdout)

if __name__ == "__main__":
    get_bluetooth_info()
