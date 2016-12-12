#!/usr/bin/env python3
import time

start = time.time()

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

contents = [x.split() for x in contents]

regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
loc = 0

def read(x):
    try:
        return int(x)
    except:
        return regs[x]

while loc < len(contents):
    inst = contents[loc]
    if inst[0] == 'cpy':
        regs[inst[2]] = read(inst[1])
    elif inst[0] == 'jnz':
        if read(inst[1]) != 0:
            loc += read(inst[2])
            loc -= 1
    elif inst[0] == 'inc':
        regs[inst[1]] += 1
    elif inst[0] == 'dec':
        regs[inst[1]] -= 1

    loc += 1

print(regs['a'])
