"""
Queue: Can be created by Array, List and LinkedList. So, it's ABT Abstracted data structure.
"""

"""
A queue is a data structure that follows the First-In-First-Out (FIFO) principle. 
An implementation of a queue using an array in Python might look like this:
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


"""
The enqueue() method appends an item to the end of the queue, and the dequeue() method removes and returns the item at 
the front of the queue. The size() method returns the number of items currently in the queue.

It is important to notice that, if there are very large number of element and frequent popping and appending of element, 
this implementation might become slow since all the elements will have to be shifted in memory. For such use case, 
ring buffer and deque can be used.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class QueueWithLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


"""
The enqueue() method creates a new node containing the data and adds it to the end of the list (i.e., after the current 
tail node), updating the tail reference to the new node. The dequeue() method removes and returns the data from the 
front of the list (i.e., the head node), updating the head reference to the next node in the list. The size() method 
returns the number of nodes in the list.

Here, It is important to note that, linked list implementaion can take less space compared to array as its dynamic and 
when number of elements are large, it can save space which can be wasted in array implementation.
"""

"""
In a queue implemented using a Python list (i.e., an array), the time complexity for the enqueue() operation is 
generally O(1), since adding an element to the end of a list typically takes constant time. The time complexity for 
the dequeue() operation is O(n), since all the remaining elements in the list have to be shifted by one position to 
fill the gap left by the removed element at the front of the list. In worst case the time complexity can be increased 
if the list is implemented with dynamic resizing.

On the other hand, in a queue implemented using a linked list, the time complexity for both the enqueue() and dequeue() 
operation is generally O(1), since adding or removing a node at the front or back of a linked list simply involves 
updating a few pointers.

The time complexity for traversing operation is O(n) for both list and linked list.

It's important to note that these complexities are based on the assumption that we are using Python built-in list and 
linked list, which have a dynamic size and their average complexities are O(1) and O(n) respectively.
"""
