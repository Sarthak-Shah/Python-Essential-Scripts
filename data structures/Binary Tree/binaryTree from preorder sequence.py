class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    idx = -1

    def buildTree(self, nodesFromPreSeq: list):
        self.idx = self.idx + 1
        # print("this is idx ==>", self.idx)
        if nodesFromPreSeq[self.idx] == -1:
            return None

        newNode = Node(nodesFromPreSeq[self.idx])
        newNode.left = self.buildTree(nodesFromPreSeq)
        newNode.right = self.buildTree(nodesFromPreSeq)

        return newNode


if __name__ == "__main__":
    nodes = [455, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.buildTree(nodes)
    print("root node data ==>> ", root.data)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# def construct_tree(nodes):
#     def helper(i):
#         if nodes[i] == -1:
#             return None
#         node = Node(nodes[i])
#         node.left = helper(i+1)
#         node.right = helper(i+2)
#         return node
#     return helper(0)
#
#
# nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
# root = construct_tree(nodes)
# print(root.val)

