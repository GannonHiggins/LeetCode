#include <iostream>
#include <vector>

/*

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

SOLVED:
runtime 0ms
memory 11.72 MB
*/
int remove_element(std::vector<int>& nums, int val) {
    int k = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != val) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}


int main() {
    std::vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
    int val = 2;
    int k = remove_element(nums, val);
    std::cout << k << std::endl;
    for (int i = 0; i < k; i++) {
        std::cout << nums[i] << " ";
    }
    return 0;

}