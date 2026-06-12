#include <iostream>
#include <vector>


/*

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

SOLVED:
runtime 0ms
memory 22.52 MB
*/

int removeDuplicates(std::vector<int>& nums) {
    int k = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (i == 0 || nums[i] != nums[i-1]) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;

}

int main() {
    std::vector<int> nums = {1, 1, 2};
    int k = removeDuplicates(nums);
    std::cout << k << std::endl;
    return 0;
}