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
  // Negative numbers are never palindromes
  if (x < 0) return false;

  // Convert number to string for easy character comparison
  const str = x.toString();
  
  // Initialize two pointers at the start and end
  let left = 0;
  let right = str.length - 1;

  // Compare characters from both ends moving inward
  while (left < right) {
    // If characters don't match, it's not a palindrome
    if (str[left] !== str[right]) {
      return false;
    }
    // Move pointers closer to the center
    left++;
    right--;
  }

  // If all characters matched, it's a palindrome
  return true;
};

console.log(isPalindrome(10)); // false
console.log(isPalindrome(121)); // true
console.log(isPalindrome(-121)); // false
