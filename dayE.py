#!/usr/bin/env python3

from hashlib import md5
import re

def myhash(mystr):
    hashed = md5(mystr.encode('utf-8')).hexdigest()
    for i in range(2016):
        hashed = md5(hashed.encode('utf-8')).hexdigest()
    return hashed

salt = "qzyelonm"
num = 0

future = {}
keys = 0


while keys < 64:
    if num not in future:
        hashed = myhash(salt + str(num))
    else:
        hashed = future[num]
        del future[num]

    match = re.search(r'(.)\1\1', hashed)
    if match:
        for i in range(num + 1, num + 1002):
            if i not in future:
                temp = myhash(salt + str(i))
                future[i] = temp
            else:
                temp = future[i]
            if match.group(0)[0] * 5 in temp:
                keys += 1
                break
    num += 1

print(num - 1)
