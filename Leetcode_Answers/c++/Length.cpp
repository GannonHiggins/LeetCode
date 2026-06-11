#include <iostream>


/*

Given a string s consists of words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.

SOLVED:
runtime 0ms
memory 8.92 MB
*/

int lengthOfLastWord(std::string s) {
    int length = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
        if (s[i] != ' ') {
            length++;
        } else {
            if (length > 0) {
                return length;
            }
        }
    }
    return length;
}

int main() {
    std::string s = "Hello World";
    std::string s2 = "   fly me   to   the moon  ";
    std::string s3 = "luffy is still joyboy";
    std::cout << lengthOfLastWord(s) << std::endl;
    std::cout << lengthOfLastWord(s2) << std::endl;
    std::cout << lengthOfLastWord(s3) << std::endl;
    return 0;
}