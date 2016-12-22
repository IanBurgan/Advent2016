#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')
del contents[1]
del contents[0]

nodes = {}

for i in contents:
    data = i.split()
    xy = data[0].split('-')
    nodes[(int(xy[1][1:]), int(xy[2][1:]))] = [int(data[1][:-1]), int(data[2][:-1]), int(data[3][:-1]), data[4]]

total = 0
for n in nodes:
    for m in nodes:
        if n != m and nodes[n][1] <= nodes[m][2] and nodes[n][1] != 0:
            total += 1

print(total)

# Printing file to calculate part 2 by hand
outFile = open('output.txt', 'w')

x = 0
y = 0

printed = 0
while printed < len(nodes):
    temp = x
    for key in nodes:
        if key == (x, y):
            if nodes[key][0] < 400 and nodes[key][1] > 0:
                outFile.write('. ')
            elif nodes[key][0] < 400:
                outFile.write('_ ')
            else:
                outFile.write('# ')
            printed += 1
            x += 1
    if temp == x:
        x = 0
        y += 1
        outFile.write('\n')

outFile.close()
