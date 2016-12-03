#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

for i in range(len(contents)):
    contents[i] = contents[i].split()
    for j in range(len(contents[i])):
        contents[i][j] = int(contents[i][j])

# formatting for part two below (remove to solve part 1)
# begin
triangles = []
for i in range(0,len(contents),3):
    one = [contents[i][0], contents[i + 1][0], contents[i + 2][0]]
    two = [contents[i][1], contents[i + 1][1], contents[i + 2][1]]
    three = [contents[i][2], contents[i + 1][2], contents[i + 2][2]]
    triangles.append(one)
    triangles.append(two)
    triangles.append(three)
contents = triangles
# end
total = 0

for i in contents:
    one = i[0]
    two = i[1]
    three = i[2]

    if one + two > three and one + three > two and two + three > one:
        total += 1

print(total)
