#include <iostream>
#include <vector>


/*

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

SOLVED:
runtime 0ms
memory 13.68 MB
*/

int search_insert(std::vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == target) {
            return i;
        }
        if (nums[i] > target) {
            return i;
        }
    }
    return nums.size();
}

int main() {
    std::vector<int> nums = {1, 3, 5, 6};
    int target = 5;
    std::cout << search_insert(nums, target) << std::endl;
    return 0;
}