'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 SOLVED:
 runtime 0ms
 memory 12.51 MB
 '''


def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)


print(same_tree([1,2,3], [1,2,3]))
print(same_tree([1,2,3], [1,2,4]))
print(same_tree([1,2,3], [1,2,3,4]))
print(same_tree([1,2,3], [1,2,3,4,5]))
print(same_tree([1,2,3], [1,2,3,4,5,6]))
print(same_tree([1,2,3], [1,2,3,4,5,6,7]))
print(same_tree([1,2,3], [1,2,3,4,5,6,7,8]))
print(same_tree([1,2,3], [1,2,3,4,5,6,7,8,9]))
print(same_tree([1,2,3], [1,2,3,4,5,6,7,8,9,10]))
