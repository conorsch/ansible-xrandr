#!/usr/bin/python
DOCUMENTATION = '''
---
module: xrandr
short_description: Wrapper for xrandr to retrieve display screen resolution settings.
author: Conor Schaefer
requirements:
  - xrandr system package installed on target host
'''

import json
import subprocess
import re


def main():
    """Call xrandr and return screen resolution."""

    module = AnsibleModule(
        argument_spec = dict(
            something = dict(aliases=['whatever'])
        )
    )

    try:
        display_info = subprocess.check_output('xrandr').split("\n")
    except OSError:
        module.fail_json(msg="xrandr is not installed.")

    # example output:
    # eDP1 connected 2560x1440+0+0 (normal left inverted right x axis y axis) 310mm x 174mm
    regex = re.compile(r'^(?P<display_name>\w+) connected (?P<resolution_as_string>(?P<horizontal_resolution>\d+)x(?P<vertical_resolution>\d+)).*')
    try:
        r = filter(regex.match, display_info)[0]
    except IndexError:
        module.fail_json(msg="no connected screens found.")

    matches = regex.match(r).groupdict()
    module.exit_json(changed=False, result=matches)


from ansible.module_utils.basic import *
main()
