class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(rootNode: TreeNode):
    if rootNode is None:
        return 0

    lh = height(rootNode.left)
    rh = height(rootNode.right)
    return max(lh, rh) + 1


# print(height(root.right))
'''
Diameter of tree = No. of nodes in the longest path between 2 leaves
Cases:
1. Tree diameter going through root node
2. Not going through root node

Height of node required here
'''


def diameter(root: TreeNode):
    if root is None:
        return 0

    leftDiam = diameter(root.left)
    leftht = height(root.left)
    rightDiam = diameter(root.right)
    rightht = height(root.right)

    selfDiam = leftht + rightht + 1
    return max(leftDiam, rightDiam, selfDiam)


"""
O(n2) time complexity since we are also calculating height along with diameter by going through each node
"""

# print(diameter(root))


# class info:
#     def __init__(self, diam, ht):
#         self.diam = diam
#         self.ht = ht
#
#
# def diamiter2(root:TreeNode):
#
#     if root is None:
#         return info(0, 0)
#
#     leftInfo = diameter(root.left)
#     rightInfo = diameter(root.right)
#
#     diam = max(max(leftInfo.diam, rightInfo.diam), leftInfo.ht + rightInfo.ht + 1)
#     ht = max(leftInfo.ht, rightInfo.ht) + 1
#
#     return info(diam, ht)
#
#
# print(diamiter2(root))


"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Steps:
1. If the tree is empty (root == None), return 0.
2. If the node has only one child, we must explore the non-null subtree because the minimum depth requires reaching a leaf node.
3. If both left and right children exist, recursively compute the minimum depth of both and return the smaller one + 1 (for the current node).
"""


def minDepth(root):
    if not root:
        return 0

    # If no left subtree, return depth of right subtree + 1
    if not root.left:
        return minDepth(root.right) + 1

    # If no right subtree, return depth of left subtree + 1
    if not root.right:
        return minDepth(root.left) + 1

    # If both subtrees exist, return the minimum depth of both
    return min(minDepth(root.left), minDepth(root.right)) + 1


# Constructing the binary tree [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# print(minDepth(root))  # Output: 2


"""
Subtree of another Tree
Given the roots of two binary trees root and subroot, return true if there is a subtree of root with the same structure and node values of subroot
and false otherwise

steps:
1. Find subroot in tree
2. check identical (subtree should be equal to the node subtree)
non - identical cases:
- node.data != subroot.data
- node = null or subroot = null
- left subtree -> non identical
- right subtree -> non-identical
"""
# The subtree "subRoot" is present in "root" starting at node with value 2


def isIdentical(root: TreeNode, subroot: TreeNode) -> bool:
    if not root and not subroot:
        return True
    if not root or not subroot or root.data != subroot.data:
        return False
    return isIdentical(root.left, subroot.left) and isIdentical(root.right, subroot.right)


def isSubtree(root: TreeNode, subroot: TreeNode) -> bool:
    if not root:
        return False
    if root.data == subroot.data and isIdentical(root, subroot):
        return True
    return isSubtree(root.left, subroot) or isSubtree(root.right, subroot)


# Create a three-level binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Create a subtree
subRoot = TreeNode(2)
subRoot.left = TreeNode(4)
subRoot.right = TreeNode(5)

print(isSubtree(root, subRoot))  # Output: True


"""
Top View of a Tree:

"""