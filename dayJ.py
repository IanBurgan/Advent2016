#!/usr/bin/env python3

num = 3001330

# part 1 Josephus Problem
print(2 * (num - 2**21) + 1)

# part 2 based upon observed pattern with smaller inputs
i = 1
while i < num:
    i *= 3
print(num - (i / 3))
