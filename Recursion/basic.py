import math
"""
One of the Core powerful concepts of any programming language.
Before Recursion, one should know 1) Iteration 2) Functions

Mostly used with advanced data structures like, Trees, Graphs, DP (dynamic programming)
It's imp to know when to use iteration and when to use recursion.  (Like tree traversal is easy
with recursion than iteration)

At every level, similar smaller problem called.

Definition:
    Recursion is a method of solving a computational problem where the solution depends on solutions to the smaller
    instances of the same problem.

Flow: 2 directions:
    1) Top to Down (towards base case)
    2) Combine solution & Go Down to Top

Call Stack:
        Stack up towards base case
        stack down towards main call (BASE CASE should be there otherwise Stack Overflow happen !)

Stack Overflow: Memory overflow 
        1) Too many recursion calls
        2) Too many parameter storage in each recursion call
(that's why base case is required while constructing recursive funtion)
"""

# Write a recursive function that prints the values from n to 1:


class RecursionForPrintDec:
    def __init__(self):
        pass

    def printDec(self, num):
        if num == 1:
            print(num)
            return None
        print(num)
        self.printDec(num-1)

    def print_n_to_1(self, n):
        if n > 0:
            print(n)
            self.print_n_to_1(n - 1)


# Example usage
# a = RecursionForPrintDec()
# a.printDec(10)
# print("################"*5)
# a.print_n_to_1(5)

# Write a recursive function that prints the values from 1 to n:
def printInc(num):
    if num == 1:
        print(num)
        return None
    printInc(num-1)
    print(num)


printInc(10)
