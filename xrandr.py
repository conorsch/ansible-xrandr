#!/usr/bin/python

import datetime
import sys
import json
import os
import shlex
import subprocess
import re



def main():

    try:
        display_info = subprocess.check_output('xrandsadr')
    except OSError:
        print("xrandr is not installed.")
        sys.exit(1)


    r = display_info.split("\n")[0]
    regex = r'.*current (?P<horizontal_resolution>\d+) x (?P<vertical_resolution>\d+),'

    matches = re.match(regex, r).groupdict()
    results = dict(changed=False, matches**)
    print(results)



