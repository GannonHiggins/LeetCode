/*

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

SOLVED:

1ms
55.17 MB memory

*/

var mySqrt = function (x) {
  // Base case: square root of 0 is 0, square root of 1 is 1
  if (x < 2) return x;

  // Newton's method (Newton-Raphson): iteratively improve guess
  // Start with initial guess y = x
  let y = x;

  // Calculate first improved guess using formula: z = (y + x/y) / 2
  let z = (y + x / y) / 2;

  // Continue until the difference between guesses is very small
  while (Math.abs(y - z) >= 0.00001) {
    // Update current guess to the new value
    y = z;

    // Calculate next improved guess
    // This formula averages y with x/y, converging toward sqrt(x)
    z = (y + x / y) / 2;
  }

  // Round down to nearest integer as required
  return Math.floor(z);
};

console.log(mySqrt(4)); // should return 2
console.log(mySqrt(8)); // should return 2
console.log(mySqrt(16)); // should return 4
console.log(mySqrt(25)); // should return 5
console.log(mySqrt(36)); // should return 6
console.log(mySqrt(49)); // should return 7
console.log(mySqrt(64)); // should return 8
console.log(mySqrt(81)); // should return 9
console.log(mySqrt(100)); // should return 10
