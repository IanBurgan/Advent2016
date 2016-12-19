#!/usr/bin/env python3

num = '01000100010010111'
# part 1 amount = 272
# part 2 amount = 35651584
amount = 272

def process(thing):
    a = thing
    b = thing[::-1]

    b = b.replace('0','x')
    b = b.replace('1', '0')
    b = b.replace('x', '1')

    return a + '0' + b

while len(num) < amount:
    num = process(num)

def csum(thing):
    check = ''
    for i in range(0,len(thing) - 1, 2):
        if thing[i] == thing[i + 1]:
            check += '1'
        else:
            check += '0'

    if len(check) % 2 == 0:
        check = csum(check)

    return check

num = num[:amount]
print(csum(num))
