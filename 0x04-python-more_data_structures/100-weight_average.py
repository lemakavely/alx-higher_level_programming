#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num_1 = 0
        num_2 = 0
        for i in my_list:
            num_1 += (i[0] * i[1])
            num_2 += i[1]
        return (num_1 / num_2)
    return 0
