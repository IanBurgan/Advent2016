#!/usr/bin/env python3

# my input
pos1, circ1 = 1, 13
pos2, circ2 = 10, 19
pos3, circ3 = 2, 3
pos4, circ4 = 1, 7
pos5, circ5 = 3, 5
pos6, circ6 = 5, 17
pos7, circ7 = 0, 11

time = 0

part2 = True
found = False
while not found:
    time += 1
    pos1 += 1
    pos2 += 1
    pos3 += 1
    pos4 += 1
    pos5 += 1
    pos6 += 1
    pos7 += 1

    if pos1 == circ1:
        pos1 = 0
    if pos2 == circ2:
        pos2 = 0
    if pos3 == circ3:
        pos3 = 0
    if pos4 == circ4:
        pos4 = 0
    if pos5 == circ5:
        pos5 = 0
    if pos6 == circ6:
        pos6 = 0
    if pos7 == circ7:
        pos7 = 0

    if pos1 == 12 and pos2 == 17 and pos3 == 0 and pos4 == 3 and pos5 == 0 and pos6 == 11:
        if not part2:
            print(time)
            found = True
        elif pos7 == 4:
            print(time)
            found = True
