#!/usr/bin/env python3

from hashlib import md5
import queue

def loc(seq):
    x = 0
    y = 0

    for i in seq:
        if i == 'R':
            x += 1
        elif i == 'L':
            x -= 1
        elif i == 'U':
            y -= 1
        elif i == 'D':
            y += 1

    return (x,y)

def check(spot):
    return spot[0] >= 0 and spot[1] >= 0 and spot[0] < 4 and spot[1] < 4

myInput = 'dmypynyp'
paths = queue.Queue()
paths.put('')

# will run infinitely for part2
part2 = True
found = False
while not found:
    mypath = paths.get()
    if loc(mypath) == (3,3):
        if not part2:
            print(mypath)
            found = True
        else:
            print(loc(mypath), len(mypath))
    else:
        thing = myInput + mypath
        options = md5(thing.encode('utf-8')).hexdigest()[:4]

        for i in range(len(options)):
            if options[i] in 'bcdef':
                if i == 0:
                    if check(loc(mypath + 'U')):
                        paths.put(mypath + 'U')
                elif i == 1:
                    if check(loc(mypath + 'D')):
                        paths.put(mypath + 'D')
                elif i == 2:
                    if check(loc(mypath + 'L')):
                        paths.put(mypath + 'L')
                elif i == 3:
                    if check(loc(mypath + 'R')):
                        paths.put(mypath + 'R')
