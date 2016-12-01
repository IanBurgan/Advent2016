#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
contents = contents.strip()
contents = contents.split(", ")

locations = set()
found = False

up = 0
right = 0

direction = 1

for i in contents:
    if i[0] == "R":
        direction += 1
        if direction == 5:
            direction = 1
    elif i[0] == "L":
        direction -= 1
        if direction == 0:
            direction = 4
    else:
        print("Error")

    if direction == 1:
        for m in range(int(i[1:])):
            up += 1
            if (up, right) not in locations:
                locations.add((up, right))
            elif not found:
                found = True
                answer2 = "Part 2: " + str(up + right)
    elif direction == 2:
        for m in range(int(i[1:])):
            right += 1
            if (up, right) not in locations:
                locations.add((up, right))
            elif not found:
                found = True
                answer2 = "Part 2: " + str(up + right)
    elif direction == 3:
        for m in range(int(i[1:])):
            up -= 1
            if (up, right) not in locations:
                locations.add((up, right))
            elif not found:
                found = True
                answer2 = "Part 2: " + str(up + right)
    elif direction == 4:
        for m in range(int(i[1:])):
            right -= 1
            if (up, right) not in locations:
                locations.add((up, right))
            elif not found:
                found = True
                answer2 = "Part 2: " + str(up + right)
    else:
        print("Error")

myfile.close()

print("Part 1:", up + right)
print(answer2)
