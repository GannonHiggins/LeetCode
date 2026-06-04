'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

SOLVED:
runtime 0ms
memory 12.37 MB
'''




def climbing_stairs(n):
    if n == 1 or n == 2:
        return n
    
    prev, curr = 1, 2
    for i in range(3, n+1):
        prev, curr = curr, prev + curr
    return curr



print(climbing_stairs(2))
print(climbing_stairs(3))
print(climbing_stairs(4))
print(climbing_stairs(5))
print(climbing_stairs(6))
print(climbing_stairs(7))
print(climbing_stairs(8))
print(climbing_stairs(9))
print(climbing_stairs(10))