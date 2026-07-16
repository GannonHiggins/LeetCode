#include <iostream>


/*
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Solved: 
0ms beats 100% of submissions
8.5MB Memory Usage beats 87.47% of submissions
*/


int mySqrt(int x) {
    // Base case: square root of 0 is 0
    if (x == 0) return 0;
    
    // Binary search bounds: search space is [1, x]
    int left = 1, right = x;
    
    // Binary search to find the largest integer whose square is <= x
    while (left <= right) {
        // Calculate mid to avoid overflow
        int mid = left + (right - left) / 2;
        
        // Use long long to prevent overflow when mid is large (e.g., x up to 2^31-1)
        long long square = (long long)mid * mid;
        
        // Perfect square found
        if (square == x) return mid;
        // mid is too small, search right half
        else if (square < x) left = mid + 1;
        // mid is too large, search left half
        else right = mid - 1;
    }
    
    // Return right as it will be the largest integer whose square is <= x
    return right;
}


int main() {
    int x = 4;
    int result = mySqrt(x);
    std::cout << "The square root of " << x << " is " << result << std::endl;
    return 0;
}
