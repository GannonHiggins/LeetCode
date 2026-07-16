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
    if (x == 0) return 0;
    int left = 1, right = x;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        long long square = (long long)mid * mid;
        if (square == x) return mid;
        else if (square < x) left = mid + 1;
        else right = mid - 1;
    }
    return right;
}


int main() {
    int x = 4;
    int result = mySqrt(x);
    std::cout << "The square root of " << x << " is " << result << std::endl;
    return 0;
}
