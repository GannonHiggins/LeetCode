/*
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do this by modifying the input array in-place with O(1) extra memory.
Custom Judge:

The judge will test your solution with the following code:
Example 1:


int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
It is sorted with no values equaling val.
int k = removeElement(nums, val); // Calls your implementation
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

SOLVED:
0ms
53.81 MB memory

*/

var removeElement = function (nums, val) {
  // k tracks the position where next valid element should be placed
  let k = 0;
  
  // Iterate through the entire array
  for (let i = 0; i < nums.length; i++) {
    // If current element is not the value to remove
    if (nums[i] !== val) {
      // Place it at position k and increment k
      // This overwrites any previous occurrences of val
      nums[k++] = nums[i];
    }
    // If nums[i] equals val, we skip it (don't increment k)
  }
  
  // k now represents the count of elements that are not equal to val
  return k;
};

console.log(removeElement([3, 2, 2, 3], 3)); // should return 2
console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)); // should return 5
console.log(removeElement([1, 2, 3, 4, 5], 3)); // should return 4
console.log(removeElement([1, 2, 3, 4, 5], 3)); // should return 4
