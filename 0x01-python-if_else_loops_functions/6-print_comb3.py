#!/usr/bin/python3
for k in range(0, 8):
    for i in range(k + 1, 10):
        print("{:d}{:d}".format(k, i), end=', ')
print("{:d}{:d}".format(k + 1, i))
