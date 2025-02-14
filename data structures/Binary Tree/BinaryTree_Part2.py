'''
Diameter of tree = No. of nodes in the longest path between 2 leaves
Cases:
1. Tree diameter going through root node
2. Not going through root node

Height of node required here
'''


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


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# print(height(root.right))


def diameter(root:TreeNode):
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
