""""
__author__ = sarthak shah
"""
"""
An ITERATOR is a data structure that provides meothds to step through all the items contained in another data structure,
visiting each item exactly once.
- I must provide atleast one method usually called next()
- other methods it provides depends on the data structure it steps through and the language used to implement it.
- The object that the iterator steps through is sometimes called an ITERABLE.
- Other benefit of ITERATOR is, they can represent infinite sequecnes.
- Python uses the term iterable, for any class that can produce an iterator.
"""


class Node(object):
    def __init__(self, datum, next=None):
        self.__data = datum  # the datum for this node
        self.__next = next  # referecne to next link

    def getData(self, datum):
        return self.__data

    def setData(self, datum):  # change the datum in this link
        self.__data = datum

    def getNext(self):
        return self.__next  # return the next node

    def setNext(self, node):
        if node is None or isinstance(node, Node):
            self.__next = node
        else:
            raise Exception("Next node must be Node or None")

    def __str__(self):  # make a string representation of node
        return str(self.getData())


class ListIterator(object):  # private iterator class
    def __init__(self, llist):  # construct an iterator over
        self._llist = llist  # linked list
        self._next = llist.getNext()  # start at first link/node

    def getData(self):
        # mocking to demonstrate iterator working
        return 9

    def getNext(self):
        # moching to deomonstrate iterator working
        return None

    def next(self):
        if self._next is None:  # check for end of list
            raise StopIteration  # at the end raise exception
        item = self._next.getData()  # store next data item
        self._next = self._next.getNext()  # advacne to following
        return item

    def iterator(self):
        return self


# llist = ListIterator(12)
# it = llist.iterator()
# print('created an iterator it', it)
#
# try:
#     while True:
#         print('The next item is: ', it.next())
# except StopIteration:
#     print('End of iterator')

"""
Generators:
- What's the need to Generators:
    Any Python object class that implements the __iter__() method becomes an iterable object.
    This iterator object must implement __next__() method. This can be written with hidden class 
    like mentioned above.
    BUT THERE IS AN EASIER WAY: GENERATORS !
    - Generators are functions that creates Iterators.
    - Python has special statement "the YIELD STATEMENT" that takes care of creating the iterator class and its required
    methods.
    
(Let's look at famous infinite sequence of fibonacci example !)
"""


# A Python generator for fibonacci sequence

def Fibonacci():
    previous = 0
    current = 1
    while True:
        yield current
        next = current + previous
        previous, current = current, next


gen = Fibonacci()
print(gen)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

"""
Here you can see, it has implemented __next__() since we have used yield statement in function. !
It pauses the execution and resume it in next call. 
"""