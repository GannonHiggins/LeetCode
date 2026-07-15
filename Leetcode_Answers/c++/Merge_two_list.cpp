#include <iostream>


/*
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


SOLVED: 
0ms Runtime
19.5Mb Memory Usage
*/

// Node structure for a singly linked list
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Recursively merge two sorted linked lists into one sorted list
ListNode* merge_two_list(ListNode* list1, ListNode* list2) {
    // Base cases: if one list is empty, return the other
    if (list1 == nullptr) return list2;
    if (list2 == nullptr) return list1;
    
    // Choose the smaller head node and recursively merge the rest
    if (list1->val < list2->val) {
        list1->next = merge_two_list(list1->next, list2);
        return list1;
    }
    else {
        list2->next = merge_two_list(list1, list2->next);
        return list2;
    }
}

int main() {
    // Create test lists: list1 = [1,2,4] and list2 = [1,3,4]
    ListNode* list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
    ListNode* list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
    
    // Merge the two sorted lists
    ListNode* result = merge_two_list(list1, list2);
    
    // Print the merged list
    while (result != nullptr) {
        std::cout << result->val << " ";
        result = result->next;
    }
    return 0;
}