#!/usr/bin/env python3

import queue

def wall(x, y):
    val = x*x + 3*x + 2*x*y + y + y*y + 1362
    return bin(val).count('1') % 2 == 1

loc = (31, 39)
visited = set()
q = queue.Queue()
q.put((1, 1, 0))

while loc not in visited:
    x, y, steps = q.get()
    # Uncomment for part 2
    # if steps > 50:
    #     print(len(visited))
    #     break
    visited.add((x,y))

    if x - 1 >= 0 and not wall(x-1, y) and (x-1, y) not in visited:
        q.put((x-1, y, steps + 1))
    if not wall(x+1, y) and (x+1, y) not in visited:
        q.put((x+1, y, steps + 1))
    if y - 1 >= 0 and not wall(x, y-1) and (x, y-1) not in visited:
        q.put((x, y-1, steps + 1))
    if not wall(x, y+1) and (x, y+1) not in visited:
        q.put((x, y+1, steps + 1))

# Comment out for part 2
print(steps)
