def remove_deplicates(nums):
    k = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_deplicates([1,1,2]))
print(remove_deplicates([0,0,1,1,1,2,2,3,3,4]))
print(remove_deplicates([]))
print(remove_deplicates([1]))
