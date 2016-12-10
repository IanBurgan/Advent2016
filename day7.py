#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()

total = 0

for i in contents:
    paran = False
    supports = False
    supports2 = False
    inside = set()
    outside = set()

    for j in range(len(i) - 2):
        if i[j] == '[':
            paran = True
        if i[j] == ']':
            paran = False
        if i[j] == i[j+2] and i[j] != i[j+1]:
            if not paran:
                if i[j] + i[j+1] in inside:
                    supports = True
                    break
                outside.add(i[j] + i[j +1])
            else:
                if i[j + 1] + i[j] in outside:
                    supports = True
                    break
                inside.add(i[j+1] + i[j])

    if supports:
        total += 1

print(total)
