/*

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


SOLVED:
33ms runtime 
54.71MB memory

*/

var twoSum = function (nums, target) {
  // Iterate through each element in the array
  for (let i = 0; i < nums.length; i++) {
    // Compare current element with all elements after it
    for (let j = i + 1; j < nums.length; j++) {
      // Check if the sum of two numbers equals the target
      if (nums[i] + nums[j] === target) {
        // Return the indices of the two numbers
        return [i, j];
      }
    }
  }
};

// Test case: should return [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
console.log(twoSum([2, 7, 11, 15], 9));
