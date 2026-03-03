'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

SOLVED:
runtime 0ms
memory 12.28 MB
beats: 100%
'''


def plus_one(digits):
    sum = int("".join(map(str, digits))) + 1
    return list(map(int, str(sum)))


print(plus_one([1, 2, 3]))
print(plus_one([4, 5, 6]))
print(plus_one([7, 8, 9]))
print(plus_one([1, 0, 0]))
print(plus_one([1, 0, 1]))
print(plus_one([1, 0, 2]))
print(plus_one([1, 0, 3]))
print(plus_one([1, 0, 4]))
print(plus_one([1, 0, 5]))  