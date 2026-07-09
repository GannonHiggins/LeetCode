#include <iostream>

/*

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

SOLVED:
0ms runtime
7.92 MB memory
*/

int climbStairs(int n) {

    int prev1 = 0;
    int prev2 = 1;

    for (int i = 0; i <= n; i++) {
        int current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    return prev1;
}



int main() {
    int n = 2;
    std::cout << climbStairs(n) << std::endl;
    return 0;
}