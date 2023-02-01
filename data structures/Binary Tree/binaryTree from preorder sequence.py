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

    def preorder_traversal(self, root_node):
        """
        It's preorder traversal as it startes with root -> left sub tree -> right sub tree
        Using recursion we can do preorder traversal. since it starts from root to leaf,
        it's called preorder traversal.
        TC would be O(n) as we traverse each node.
        """
        if root_node is None:
            print("-1", end="\t")
            return
        print(root_node.data, end="\t")
        self.preorder_traversal(root_node.left)
        self.preorder_traversal(root_node.right)

    def inorder_traversal(self, root_node):
        """
        It's inorder traversal as it startes from left subtree -> root -> right subtree
        Using recursion will do inorder traversal.
        TC  O(n)
        """
        if not root_node:
            return
        self.inorder_traversal(root_node.left)
        print(root_node.data, end="\t")
        self.inorder_traversal(root_node.right)


    def postorder_traversal(self, root_node):
        """
        it starts from left subtree -> right sub tree -> root
        """
        if not root_node:
            return
        self.postorder_traversal(root_node.left)
        self.postorder_traversal(root_node.right)
        print(root_node.data, end="\t")


if __name__ == "__main__":
    nodes = [455, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.buildTree(nodes)
    print("root node data ==>> ", root.data)
    print("------------- Preorder traversal ---------------")
    tree.preorder_traversal(root)
    print("\n------------- Inorder traversal ---------------")
    tree.inorder_traversal(root)
    print("\n------------- Postorder traversal ---------------")
    tree.postorder_traversal(root)

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
