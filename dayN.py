#!/usr/bin/env python3
import time

start = time.time()

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

contents = [x.split() for x in contents]

regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
loc = 0

def read(x):
    try:
        return int(x)
    except:
        return regs[x]

while loc < len(contents):
    inst = contents[loc]

    # multiply rather than complete long loop
    if loc == 4:
        regs['a'] = regs['b'] * regs['d']
        loc = 10
        continue

    if inst[0] == 'cpy':
        if inst[2] in regs:
            regs[inst[2]] = read(inst[1])
    elif inst[0] == 'jnz':
        if read(inst[1]) != 0:
            loc += read(inst[2])
            loc -= 1
    elif inst[0] == 'inc':
        regs[inst[1]] += 1
    elif inst[0] == 'dec':
        regs[inst[1]] -= 1
    elif inst[0] == 'tgl':
        toggle = loc + read(inst[1])
        if toggle < len(contents):
            if contents[toggle][0] == 'inc':
                contents[toggle][0] = 'dec'
            elif contents[toggle][0] == 'dec':
                contents[toggle][0] = 'inc'
            elif contents[toggle][0] == 'jnz':
                contents[toggle][0] = 'cpy'
            elif contents[toggle][0] == 'tgl':
                contents[toggle][0] = 'inc'
            else:
                contents[toggle][0] = 'jnz'

    loc += 1

print(regs['a'])
