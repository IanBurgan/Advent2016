#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()

contents = contents[0]

total = 0
i = 0
while i < len(contents):
    if contents[i] == '(':
        # chars is the number between current location, which is (, and x
        chars = int(contents[i + 1:contents[i:].find('x')+i])
        # amount is the number between x and )
        amount = int(contents[contents[i:].find('x')+1+i:contents[i:].find(')')+i])
        # add the amount to the total
        total += chars * amount
        # move i past the marker and the characters affected by the marker
        i = contents[i:].find(')') + chars + i + 1
    else:
        total += 1
        i += 1

print(total)
