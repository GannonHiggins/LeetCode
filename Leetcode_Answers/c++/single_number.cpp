#include <iostream>
#include <vector>

/* 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Solved: 
0ms beats 100% of submissions
20.65MB Memory Usage beats 58.95% of submissions

*/


int singleNumber(std::vector<int>& nums) {
    // Initialize result to 0 (identity element for XOR)
    int result = 0;
    
    // XOR all numbers together
    // Key properties: a ^ a = 0 and a ^ 0 = a
    // Since every number appears twice except one, pairs cancel out (XOR to 0)
    // Only the single number remains
    for (int num : nums) {
        result ^= num;
    }
    
    return result;
}

int main() {
    std::vector<int> nums = {4,1,2,1,2};
    int result = singleNumber(nums);
    std::cout << "The single number is " << result << std::endl;
    return 0;
}