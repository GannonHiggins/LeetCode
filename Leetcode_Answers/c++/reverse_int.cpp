#include <iostream>

/*

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

SOLVED:
runtime 5ms
memory 8.59 MB
*/

int reverse_int(int x){
    long long rev = 0;
    while (x != 0) {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    if (rev > 2147483647 || rev < -2147483648) return 0;
    return (int)rev;
}

int main() {
    int x = -123;
    std::cout << reverse_int(x) << std::endl;
    return 0;
}