'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

SOLVED
runtime 3ms
memory 12.52 MB
'''

def square_root(x):
    if x < 2:
        return x
    lo, hi = 1, x
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

print(square_root(4))
print(square_root(8))
print(square_root(16))
print(square_root(25))
print(square_root(36))
print(square_root(49))
print(square_root(64))
print(square_root(81))
print(square_root(100))