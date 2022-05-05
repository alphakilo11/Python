#!/usr/bin/env python3
import json

with open('test.txt') as json_file:
    data = json.load(json_file)
#    print(data)
#    pretty print
#    print(json.dumps(data, indent=4))
print(len(data))
for i, k in data.items():
    for j in range(10):
        print(k[j])