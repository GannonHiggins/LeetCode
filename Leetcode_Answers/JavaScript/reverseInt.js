/*
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:
Input: x = 123
Output: 321


Example 2:
Input: x = -123
Output: -321


Example 3:
Input: x = 120
Output: 21

SOLVED:
50ms runtime beats 65.52% of users with JavaScript
55.95MB memory beats 51.02% of users with JavaScript

*/

var reverseInt = function (x) {
  let reversed = 0;
  const INT_MAX = 2 ** 31 - 1;
  const INT_MIN = -(2 ** 31);

  while (x !== 0) {
    let digit = x % 10;
    x = Math.trunc(x / 10);
    reversed = reversed * 10 + digit;
  }

  if (reversed > INT_MAX || reversed < INT_MIN) return 0;
  return reversed;
};

console.log(reverseInt(123));
console.log(reverseInt(-123));
console.log(reverseInt(120));
