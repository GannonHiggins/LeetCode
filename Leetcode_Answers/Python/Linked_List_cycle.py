'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

SOLVED:
runtime 27ms
memory 19.43 MB
beats: 67.76%
'''

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(hasCycle([1,2,3,4,5]))
print(hasCycle([1,2,3,4,5,6]))
print(hasCycle([1,2,3,4,5,6,7,8,9,10]))