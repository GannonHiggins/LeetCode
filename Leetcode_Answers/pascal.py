'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

SOLVED:
runtime 0ms
memory 12.34 MB
'''

def generate(numRows):
    pascal = [[1]]
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        row.append(1)
        pascal.append(row)
    return pascal

print(generate(5))
