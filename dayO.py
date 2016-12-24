#!/usr/bin/env python3

import queue
from itertools import permutations

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

def find_spot(symbol):
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if contents[i][j] == symbol:
                return (i, j)

moves = set([(1, 0), (-1, 0), (0, 1), (0, -1)])
def search(origin, to):
    log = queue.Queue()
    log.put((0, origin))
    visited = set([origin])

    while True:
        dist, loc = log.get()

        if loc == to:
            return dist

        x, y = loc
        for dx, dy in moves:
            newx, newy = x + dx, y + dy
            if contents[newx][newy] != '#' and (newx, newy) not in visited:
                log.put((dist + 1, (newx, newy)))
                visited.add((newx, newy))


zero = find_spot('0')
nums = [find_spot(str(i)) for i in range(1, 8)]
dist0 = [search(zero, num) for num in nums]

dists = [[None for i in range(7)] for j in range(7)]

for i in range(7):
    for j in range(i + 1, 7):
        dists[i][j] = search(nums[i], nums[j])
        dists[j][i] = dists[i][j]

lengths1 = []
lengths2 = []

for path in permutations(range(7)):
    dist = dist0[path[0]]

    for i in range(len(path) - 1):
        dist += dists[path[i]][path[i + 1]]
    lengths1.append(dist)
    dist += dist0[path[-1]]
    lengths2.append(dist)

print(min(lengths1))
print(min(lengths2))
