#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

contents = set(contents)
temp = set()

bots = {}
outputs = {}

while len(contents) > 0:
    inst = contents.pop().split()
    if inst[0] == 'value':
        if inst[-1] not in bots:
            bots[inst[-1]] = [int(inst[1])]
        else:
            bots[inst[-1]].append(int(inst[1]))
    else:
        temp.add(' '.join(inst))

contents.update(temp)
temp = set()

def attempt(robot, low, high):
    if robot in bots and len(bots[robot]) > 1:
        success = True
        lowNum = min(bots[robot])
        highNum = max(bots[robot])
        bots[robot] = []

        if lowNum == 17 and highNum == 61:
            print(robot)

        if low[0] != 'o':
            if low in bots:
                bots[low].append(lowNum)
            else:
                bots[low] = [lowNum]
        else:
            if low in outputs:
                outputs[low].append(lowNum)
            else:
                outputs[low] = [lowNum]

        if high[0] != 'o':
            if high in bots:
                bots[high].append(highNum)
            else:
                bots[high] = [highNum]
        else:
            if high in outputs:
                outputs[high].append(highNum)
            else:
                outputs[high] = [highNum]
    else:
        success = False

    return success

while len(contents) > 0:
    inst = contents.pop().split()
    robot = inst[1]
    low = inst[6]
    high = inst[-1]

    if inst[5] == 'output':
        low = 'output' + low
    if inst[-2] == 'output':
        high = 'output' + high

    if not attempt(robot, low, high):
        temp.add(' '.join(inst))

    if len(contents) == 0:
        contents.update(temp)
        temp = set()

print(outputs['output0'][0] * outputs['output1'][0] * outputs['output2'][0])
