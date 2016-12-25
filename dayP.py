#!/usr/bin/env python3
import time

start = time.time()

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

contents = [x.split() for x in contents]

def test(num):
    output = ''
    regs = {'a': num, 'b': 0, 'c': 0, 'd': 0}
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
        elif inst[0] == 'out':
            output += str(read(inst[1]))
            if len(output) > 10:
                return output

        loc += 1

for i in range(350):
    out = test(i)
    if out == '01010101010':
        print(i)
        break
