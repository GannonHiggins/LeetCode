'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


SOLVED:
runtime 2ms
memory 12.34 MB
beats: 92.03%

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addtwoNumbers(l1, l2):
    carry = 0
    result = ListNode(0)
    current = result
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return result.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(addtwoNumbers(l1, l2))