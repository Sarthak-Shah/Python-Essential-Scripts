class CreateNode:
    def __init__(self, data, pointer):
        self.data = data
        self.next = pointer


class LinkedList:
    def __init__(self):
        # it initializes empty linked list
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, data):
        # it adds the Node to the starting. or prepend the Node. or to adds to the left.
        oldFirst = self.head
        newNode = CreateNode(data, oldFirst)
        self.head = newNode
        if self.tail is None:
            self.tail = newNode
        self.size += 1

    def addLast(self, data):
        oldLast = self.tail.next
        newNode = CreateNode(data, oldLast)
        self.tail.next = newNode
        self.tail = newNode
        if self.head is None:
            self.head = newNode
        self.size += 1


    def addMiddle(self, idx: int, data):
        if self.size == 0:
            self.addFirst(data)
            return
        temp = self.head
        i = 0
        previousNode = self.head
        while i < idx:
            previousNode = temp
            temp = temp.next
            i += 1
        newNode = CreateNode(data, previousNode.next)
        previousNode.next = newNode
        self.size += 1


    def print(self):
        """

        it traverse the linked list and print its data
        """
        temp = self.head
        i = 0
        while temp is not None:
            print(f"data of Node {i} ==>> {temp.data}")
            temp = temp.next
            i += 1

    def len(self):
        print(f"this linked list has {self.size} Nodes !")


s = LinkedList()
# print(s.head, s.tail)
s.addFirst("first data")
# print("now head: ",s.head.data, "now tail: ", s.tail.data)
s.addFirst("2")
# print("now head: ",s.head.data, "now tail: ", s.tail.data)
s.addFirst("3")
# print("now head: ",s.head.data, "now tail: ", s.tail.data)
s.addLast("1")
s.addMiddle(1,"MC Square")
print("now head: ",s.head.data, "now tail: ", s.tail.data)
s.print()
s.len()
