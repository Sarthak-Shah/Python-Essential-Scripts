import math
"""find factorial of n integer"""

def findFactorial(num:int):
    if num == 0:
        return 1
    fct = num * findFactorial(num-1)
    return fct

# print(findFactorial(5))


"""
print sum of n first natural numbers.
"""


def findSum(num:int):
    if num == 1:
        return 1
    asum = num + findSum(num-1)
    return asum

# print(findSum(5))


"""
print Nth fibonacci number
fib(n) = fib(n-1) + fib(n-2)
multiple recursion calls forms tree like structure in call stack.
space complexity: O(n)
time complexity: O(2^n) (exponential)
It can be solved by DP. (dynamic programming to make it linear by storing already computed answers)
"""


def findFib(num:int):
    if num == 0 or num == 1:
        return num
    fib = findFib(num-1) + findFib(num-2)
    return fib


print(findFib(16))