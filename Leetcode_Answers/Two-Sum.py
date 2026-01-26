'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

SOLVED: 

runtime 2139ms
'''

def twosums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(twosums([2,7,11,15], 9))
print(twosums([3,2,4], 6))
print(twosums([3,3], 6))
print(twosums([2,5,5,11], 10))
