class BinarySearchTree(object):

    def __init__(self):
        """
        Tree organized nodes by their keys.
        Initially it is empty
        """
        self.__root = None

    class __Node(object):
        def __init__(self, key, data, left=None, right=None):
            self.key = key
            self.data = data
            self.leftchild = left
            self.rightchild = right

        def __str__(self):
            return "{" + str(self.key) + " , " + str(self.data) + "}"

    def isEmpty(self):
        return self.__root is None

    def root(self):
        if self.isEmpty():
            raise Exception("No root node in empty tree")
        return self.__root.data, self.__root.key

    # Finding a Node
    def __find(self, goal):
        current = self.__root
        parent = self
        while current and goal != current.key:
            parent = current
            current = (current.leftchild if goal < current.key else current.rightchild)
        return (current, parent)

    def search(self, goal):
        """
        Efficienncy: Time required to find the node depends on the depth of tree and how much tree is balanced.
        O(logN) time for balanced tree
        O(N) time for completely unbalanced tree.
        """
        node, p = self.__find(goal)
        return node.data if node else None

    # Inserting a Node
    def insert(self, key, data):
        node, parent = self.__find(key)
        if node:
            node.data = data
            return False

        if parent is self:
            self.__root = self.__Node(key, data)
        elif key < parent.key:
            parent.leftchild = self.__Node(key, data, right=node)
        else:
            parent.rightchild = self.__Node(key, data, right=node)
        return True

    # Traversing a tree
    # 1. Pre-order, 2. in-order 2. Post-order
    # for binary search tree, most common is in-order

    # Recursion is used for traversal.
    # 1. call itself to travers node's left subtree
    # 2. visit the node.
    # 3. call itself to traverse the node's right subtree
    # Recursive implementation of inOrderTraverse()

    def inOrderTraverse(self, function=print):
        self.__inOrderTraverse(self.__root, function=function)

    def __inOrderTraverse(self, node, function):
        if node:
            self.__inOrderTraverse(node.leftchild, function)
            function(node)
            self.__inOrderTraverse(node.rightchild, function)
            