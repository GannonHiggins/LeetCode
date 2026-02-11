def add_Binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]



print(add_Binary("11", "1"))
print(add_Binary("1010", "1011"))