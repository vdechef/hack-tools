#!/usr/bin/python

# based on python-registry module : https://github.com/williballenthin/python-registry

import sys
from Registry import Registry

def rec(key, printvals, keyword=None, depth=0):
    path = key.path()

    if keyword is None or keyword in path:
        print "\t" * depth + path
        if printvals:
            for value in [v for v in key.values() if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ]:
                print "%s: %s" % (value.name(), value.value())

    for subkey in key.subkeys():
        rec(subkey, printvals, keyword, depth + 1)

print "Usage: python printregistry.py <reg file> <print values> [keyword]\n\t printvalues is an integer, set to 0 or 1\n\t keyword is optional"
reg = Registry.Registry(sys.argv[1])

keyword = None if len(sys.argv) < 4 else sys.argv[3]
printval = False if sys.argv[2] == "0" else True
rec(reg.root(), printval, keyword)

