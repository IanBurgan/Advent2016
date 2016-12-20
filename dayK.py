#!/usr/bin/env python3

from operator import itemgetter

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

ranges = []

for i in range(len(contents)):
    ranges.append((int(contents[i].split('-')[0]), int(contents[i].split('-')[1])))

ranges = sorted(ranges, key=itemgetter(1))

total = 0

first = True
count = 0

# max value in my file
while count < 4272688785:
    for i in ranges:
        if count <= i[1] and count >= i[0]:
            count = i[1] + 1
    if first:
        print('Part 1:', count)
        first = False
    total += 1
    count += 1

print('Part 2:', total)
