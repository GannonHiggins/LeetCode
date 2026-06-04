#include <iostream>
#include <string>
#include <algorithm>

/*

Given an integer x, return true if x is a palindrome, and false otherwise.

SOLVED:
runtime 11ms
memory 10.76 MB
*/


bool isPalindrome(int x) {
    std::string str = std::to_string(x);
    std::string reversed = str;
    std::reverse(reversed.begin(), reversed.end());
    return str == reversed;
}

int main() {
    std::cout << isPalindrome(121) << std::endl;
    std::cout << isPalindrome(-121) << std::endl;
    std::cout << isPalindrome(10) << std::endl;
    return 0;
}