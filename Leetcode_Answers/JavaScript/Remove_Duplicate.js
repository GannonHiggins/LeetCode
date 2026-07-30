/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


SOLVED:
Runtime: 0ms
Memory: 57.04MB

*/

var removeDuplicates = function (nums) {
  let k = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[i - 1]) {
      k++;
      nums[k] = nums[i];
    }
  }
  return k + 1;
};

const nums = [1, 1, 2];
const k = removeDuplicates(nums);
console.log(k);
console.log(nums);
