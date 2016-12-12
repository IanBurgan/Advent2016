"""

Given my specific inputs, this can be solved by hand. I was only able to figure
this out by looking at the solutions of others online.

Although this may not work for all inputs, I used to following process:

My input starts with 4 items on the first floor, 2 items on the second, and 4
items on the third floor.

Using this, we can see it will take 5 moves to put the 4 items on the first onto
the second floor (2 * 4 - 3 = 5). Now that there are 6 items on the second floor
it will take 9 moves to get them all to the third floor (2 * 6 - 3 = 9). Finally,
moving all 10 items onto the fourth floow requires 17 moves (2 * 10 - 3 = 17).

My answer: 5 + 9 + 17 = 31

The same process worked for part 2. 

"""
