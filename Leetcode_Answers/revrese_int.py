'''

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

SOLVED:
runtime 0ms
beats: 26.77%
memory 12.34 MB
beats: 14.29%
'''


def reverse_int(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if x == 0:
        return 0
    if x < 0:
        rev = -reverse_int(-x)
    else:
        rev = int(str(x)[::-1])
    if rev < INT_MIN or rev > INT_MAX:
        return 0
    return rev

print(reverse_int(123))
print(reverse_int(-123))
print(reverse_int(120))
print(reverse_int(0))
print(reverse_int(1534236469))
