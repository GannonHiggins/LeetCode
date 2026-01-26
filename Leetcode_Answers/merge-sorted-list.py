'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

SOLVED:

runtime 0ms
'''



def merge_sorted_list(list1, list2):
    # Dummy node avoids special-casing the head; we build the merged list from dummy.next
    dummy = ListNode() #defiend in leetcode
    tail = dummy

    # Compare heads of both lists and append the smaller node to the merged list
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            tail = list1
            list1 = list1.next
        else:
            tail.next = list2
            tail = list2
            list2 = list2.next

    # Attach any remaining nodes from the non-empty list
    tail.next = list1 if list1 else list2
    return dummy.next


print(merge_sorted_list([1,2,4], [1,3,4]))
print(merge_sorted_list([], []))
print(merge_sorted_list([], [0]))