""""""
"""
Count Good Nodes in Binary Tree
Given the root of a binary tree, find the number of nodes that are good. 
A node is good if the path between the root and the node has no nodes with a greater value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countGoodNodes(root, max_val=float('-inf')):
    if not root:
        return 0

    # A node is good if its value is greater than or equal to max_val seen so far
    good = 1 if root.val >= max_val else 0

    # Update the maximum value along the path
    max_val = max(max_val, root.val)

    # Recursively check left and right subtrees
    good += countGoodNodes(root.left, max_val)
    good += countGoodNodes(root.right, max_val)

    return good

"""
        3
       / \
      1   4
     /   / \
    3   1   5

"""

# Create sample tree
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

# Test function
print(countGoodNodes(root))  # Expected Output: 4


"""
Same Tree
Given the roots of two binary trees p and q, check if they are the same tree. 
Two binary trees are the same tree if they are structurally identical and the nodes have the same values.
"""


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right