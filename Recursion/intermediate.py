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


# print(findFib(16))

"""
Check if array is sorted or not (ascending)
time complexity: O(n)
Space complexity: O(n) (n calls for n sized array so n + n = 2n can be considered as n)
"""


def isSorted(arr:tuple, starting:int):
    if starting == len(arr) -1:
        return True
    if arr[starting] > arr[starting+1]:
        return False
    return isSorted(arr, starting+1)


# print(isSorted((1,2,5,4), 0))


"""
Find first occurence of an element in the array
time complexity: O(n) for non existent or last element
space complexity: O(n) for non existent or last element
"""


def firstOcurrence(arr:tuple, key:int, starting:int):
    if starting == len(arr):
        return -1
    if arr[starting] == key:
        return starting
    return firstOcurrence(arr, key, starting+1)


# print(firstOcurrence((2, 4, 5, 3, 4, 5, 3), 3, 0))


"""
find last occurence in the array
"""


def lastOcurrence(arr:tuple, key:int, starting:int):
    if starting == len(arr):
        return -1
    result = lastOcurrence(arr, key, starting+1)
    if result == -1 and arr[starting] == key:
        return starting
    return result


# print(lastOcurrence((1, 2, 3, 2, 3), 2, 0))


"""
print x to the power n
tc = O(n)
can you optimize it ?
"""


def power(x:int, n:int):
    if n == 0:
        return 1
    result = x * power(x, n-1)
    return result

# print(power(2,10))


