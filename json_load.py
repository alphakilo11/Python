#!/usr/bin/env python3
import json

with open('test.txt') as json_file:
    data = json.load(json_file)
#    print(data)
#    pretty print
#    print(json.dumps(data, indent=4))