#!/usr/bin/python3
for k in range(0, 8):
    for l in range(k + 1, 10):
        print("{:d}{:d}".format(k, l), end=', ')
print("{:d}{:d}".format(k + 1, l))
