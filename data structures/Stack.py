"""
Stacks: Can be created by Array, List and LinkedList. So, it's ABT Abstracted data structure.
"""
"""
stacks follows LIFO. Last in First Out.
So to add new thing in constant time, O(1) on top, we need to push right ? ex, stack of books on table, clothes
To remove new thing in constant time, O(1) on top, pop it. 
Peek means top item. 
push, pop, peek (top), isEmpty 
"""

"""
Stack by List
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())  # prints 3
# print(stack.pop())   # prints 3
# print(stack.pop())   # prints 2
# print(stack.is_empty())  # prints False
# print(stack.pop())   # prints 1
# print(stack.is_empty())  # prints True

"""
Stack by LinedList
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        if self.top:
            return self.top.value

    def is_empty(self):
        return self.top is None


stack = Stack()
stack.push("avatar movie")
stack.push("sarthak")
stack.push("epic sports")
print(stack.peek())  # prints 3
print(stack.pop())   # prints 3
print(stack.pop())   # prints 2
print(stack.is_empty())  # prints False
print(stack.pop())   # prints 1
print(stack.is_empty())  # prints True


"""
In a stack implemented using a list data structure, the time complexity for the push and pop operations is O(1), because 
these operations can be performed in constant time by simply appending to or removing from the end of the list.

In a stack implemented using a linked list data structure, the time complexity for the push and pop operations is also O(1), 
because these operations can be performed in constant time by simply adding a new node to the front of the linked list 
or removing the front node.

So, in both cases, the time complexity for the push and pop operations is O(1). However, the linked list implementation 
has the advantage of not requiring the extra space overhead of storing the capacity of the stack, as the list 
implementation does. This can make the linked list implementation more memory efficient in some cases.
"""
