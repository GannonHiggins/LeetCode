'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


SOLVED:
runtime 74ms
memory 14.11 MB
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        node, path_sum = stack.pop()
        if not node.left and not node.right and path_sum == targetSum:
            return True
        if node.right:
            stack.append((node.right, path_sum + node.right.val))
        if node.left:
            stack.append((node.left, path_sum + node.left.val))
    return False


root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print(hasPathSum(root, 22))
