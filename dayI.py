#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = [char for char in contents]

tiles = [[]]
for i in contents:
    if i == '.':
        tiles[0].append(True)
    else:
        tiles[0].append(False)

def nextRow(row):
    below = [True] * 100
    for i in range(len(below)):
        # l and c not r
        if i > 0 and not row[i - 1] and not row[i]:
            if i == len(row) - 1:
                below[i] = False
            elif row[i + 1]:
                below[i] = False

        # c and r not l
        if not row[i] and i < len(row) - 1 and not row[i + 1]:
            if i == 0:
                below[i] = False
            elif row[i - 1]:
                below[i] = False
        # only l
        if i > 0 and not row[i - 1] and row[i]:
            if i == len(row) - 1:
                below[i] = False
            elif row[i + 1]:
                below[i] = False
        # only r
        if i < len(row) - 1 and not row[i + 1] and row[i]:
            if i == 0:
                below[i] = False
            elif row[i - 1]:
                below[i] = False

    return below

count = 0

while len(tiles) < 400000:
    tiles.append(nextRow(tiles[count]))
    count += 1

total = 0
for i in tiles:
    for j in i:
        if j:
            total += 1

print(total)
