#!/usr/bin/env python3

import itertools

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def swapp(pswd, one, two):
    temp = pswd[one]
    pswd[one] = pswd[two]
    pswd[two] = temp

def swapl(pswd, one, two):
    for i in range(len(pswd)):
        if pswd[i] == one:
            pswd[i] = two
        elif pswd[i] == two:
            pswd[i] = one

def rotate(pswd, right, num):
    if right:
        for i in range(num):
            temp = pswd.pop()
            pswd.insert(0, temp)
    else:
        for i in range(num):
            temp = pswd[0]
            del pswd[0]
            pswd.append(temp)

def rotatel(pswd, letter):
    loc = pswd.index(letter)
    rotate(pswd, True, loc + 1)
    if loc >= 4:
        rotate(pswd, True, 1)

def rev(pswd, begin, stop):
    a = pswd[begin:stop + 1]
    a = a[::-1]
    return pswd[:begin] + a + pswd[stop + 1:]

def move(pswd, one, two):
    letter = pswd[one]
    del pswd[one]
    pswd.insert(two, letter)

def solve(word, contents):
    for i in contents:
        inst = i.split()
        if inst[0] == 'swap':
            if inst[1] == 'position':
                swapp(word, int(inst[2]), int(inst[-1]))

            elif inst[1] == 'letter':
                swapl(word, inst[2], inst[-1])

        elif inst[0] == 'rotate':
            if inst[1] == 'based':
                rotatel(word, inst[-1])
            elif inst[1] == 'left':
                rotate(word, False, int(inst[2]))
            elif inst[1] == 'right':
                rotate(word, True, int(inst[2]))

        elif inst[0] == 'reverse':
            word = rev(word, int(inst[2]), int(inst[-1]))

        elif inst[0] == 'move':
            move(word, int(inst[2]), int(inst[-1]))
        else:
            print(inst)

    return ''.join(word)

print('Part 1:', solve(word, contents))

# not the best way to unsolve, but this was faster to type
for i in itertools.permutations(word):
    if solve(list(i), contents) == 'fbgdceah':
        print('Part 2:', ''.join(i))
        break
