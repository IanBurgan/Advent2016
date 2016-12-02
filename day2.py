#!/usr/bin/env python3

# only works for part 2 becuase I didn't preserve the code
# that I used for part 1
myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.split()

buttons = [[1], [2, 3, 4], [5, 6, 7, 8, 9], ['A', 'B', 'C'], ['D']]

location = [2,0]

for i in contents:
    for j in i:
        if j == "U":
            if location[0] != 0:
                if location[0] < 3 and location[1] != 0:
                    location[0] -= 1
                    location[1] -= 1

                if location[0] >= 3:
                    location[0] -= 1
                    location[1] += 1
        if j == "D":
            if location[0] != 4:
                if location[0] > 1:
                    if location[1] != 0 and location[1] != len(buttons[location[0]]) - 1:
                        location[0] += 1
                        location[1] -= 1
                else:
                    location[0] += 1
                    location[1] += 1
        if j == "R":
            if location[0] == 0:
                pass
            if location[0] == 1 and location[1] < 2:
                location[1] += 1
            if location[0] == 2 and location[1] < 4:
                location[1] += 1
            if location[0] == 3 and location[1] < 2:
                location[1] += 1
            if location[0] == 4:
                pass

        if j == "L":
            if location[1] > 0:
                location[1] -= 1

    print(buttons[location[0]][location[1]])
