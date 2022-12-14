#!/usr/bin/python3
def roman_to_int(roman_num):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(roman_num):
        if i + 1 < len(roman_num) and roman_num[i: i + 2] in roman_numbers:
            num += roman_numbers[roman_num[i: i + 2]]
            i += 2
        else:
            num += roman_numbers[roman_num[i]]
            i += 1
    return num
