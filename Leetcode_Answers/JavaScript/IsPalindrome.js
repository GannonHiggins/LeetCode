/*

Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

SOLVED:
4ms
64.68 MB memory

*/

var isPalindrome = function (x) {
  if (x < 0) return false;

  const str = x.toString();
  let left = 0;
  let right = str.length - 1;

  while (left < right) {
    if (str[left] !== str[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
};

console.log(isPalindrome(10)); // false
console.log(isPalindrome(121)); // true
console.log(isPalindrome(-121)); // false
