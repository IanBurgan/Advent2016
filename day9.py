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

# part 2
# inspired by /u/blockingthesky
def parse(contents):
    total = 0

    while '(' in contents:
        total += contents.find('(')
        contents = contents[contents.find('('):]
        chars = int(contents[1:contents.find(')')].split('x')[0])
        amount = int(contents[1:contents.find(')')].split('x')[1])
        contents = contents[contents.find(')')+1:]
        total += parse(contents[:chars]) * amount
        contents = contents[chars:]

    total += len(contents)
    return total

print(parse(contents))
