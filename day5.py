#!/usr/bin/env python3

from hashlib import md5

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()

password = [',', ',', ',', ',', ',', ',', ',', ',']
contents = 'wtnhxymk'
total = 0

# setup to work for part 2
while ',' in password:
    temp = contents + str(total)
    if md5(temp.encode('utf-8')).hexdigest()[:5] == '00000':
        hashed = md5(temp.encode('utf-8')).hexdigest()
        if hashed[5] in '01234567':
            spot = int(hashed[5])
            print(spot)
            if password[spot] == ',':
                password[spot] = hashed[6]
                print(password)
    total += 1



print(''.join(password))
