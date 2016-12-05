#!/usr/bin/env python3
from string import ascii_lowercase

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()

total = 0

for i in contents:
    num = i[-10:-7]
    check = i[-6:-1]
    seg = i[:-10].replace('-', '')

    letters = []
    counts = []
    for i in seg:
        if i not in letters:
            letters.append(i)
    letters.sort()

    for i in letters:
        counts.append(seg.count(i))

    valid = ""
    for i in range(5):
        pos = counts.index(max(counts))
        valid += letters[pos]
        del counts[pos]
        del letters[pos]

    if valid == check:
        total += int(num)

        # part 2
        renamed = ""
        for i in seg:
            shifted = ord(i) + (int(num) % 26)
            if shifted > 122:
                shifted -= 26
            renamed += chr(shifted)

        if 'north' in renamed:
            print(renamed)
            print(num)


print(total)
