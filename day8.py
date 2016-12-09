#!/usr/bin/env python3

def rect(a,b,lights):
    for i in range(a):
        for j in range(b):
            lights[j][i] = 1

def shiftRow(r, n, lights):
    lights[r] = lights[r][-n:] + lights[r][:-n]

def shiftCol(c, n, lights):
    six = ''
    for i in range(len(lights)):
        six += str(lights[i][c])

    six = six[-(n%6):] + six[:-(n%6)]

    for i in range(len(lights)):
        lights[i][c] = int(six[i])


lights = [[0] * 50, [0] * 50, [0] * 50, [0] * 50, [0] * 50, [0] * 50]

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

for i in contents:
    inst = i.split()

    if inst[0] == 'rect':
        a = int(inst[1][:-2])
        b = int(inst[1][-1])
        rect(a,b,lights)

    elif inst[1] == 'row':
        r = int(inst[2][2:])
        n = int(inst[-1])
        shiftRow(r,n,lights)

    elif inst[1] == 'column':
        c = int(inst[2][2:])
        n = int(inst[-1])
        shiftCol(c,n,lights)

total = 0

for i in range(len(lights)):
    for j in range(len(lights[i])):
        if lights[i][j] == 1:
            total += 1
            lights[i][j] = '#'
        else:
            lights[i][j] = ' '

print(total)

for i in lights:
    print(''.join(i))
