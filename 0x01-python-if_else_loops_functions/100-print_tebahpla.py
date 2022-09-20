#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((x - (ord('a') - ord('A'))) if x % 2 else x), end='')
