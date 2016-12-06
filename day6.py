#!/usr/bin/env python3
from collections import Counter

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()

word1 = ''
word2 = ''

for i in zip(*contents):
    word1 += Counter(i).most_common()[0][0]
    word2 += Counter(i).most_common()[-1][0]


print(word1)
print(word2)
