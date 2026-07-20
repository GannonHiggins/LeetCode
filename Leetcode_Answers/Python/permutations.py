"""
LeetCode 46. Permutations

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

SOLVED: 
0ms runtime, beats 100%
19.42MB memory, beats 65.43%
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            for perm in self.permute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + perm)
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3]
    print(f"Input: {nums1}")
    print(f"Output: {solution.permute(nums1)}")
    print()
    
    # Test case 2
    nums2 = [0, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.permute(nums2)}")
    print()
    
    # Test case 3
    nums3 = [1]
    print(f"Input: {nums3}")
    print(f"Output: {solution.permute(nums3)}")
