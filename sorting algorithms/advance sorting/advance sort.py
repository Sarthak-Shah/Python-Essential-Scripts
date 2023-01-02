"""
Radix sort: base (used) for sorting. non comparison algorithm.
space and time complexity depends on max length of digit from array.
start from RSB or LSB iterate through it and allocate it into respective bucket(bin) ex. 0 to 9 for base 10.

time complexity: Radix sort has a time complexity of O(n*m), where n is the size of the input list and m is the maximum
number of digits in the elements of the list.
Therefore, it’s not necessarily that O(n*m) is always faster than O(n*log(n)). It depends on the comparison between m
and log(n).
space complexity: Radix sort has a space complexity of O(n + b), where n is the size of the input list and b is the
base (radix) used for sorting. Because the algorithm requires additional space to store the list of buckets used to
sort the elements.
"""


def radix_sort(arr):
    """
    Radix sort starting from the least significant digit(LSD)
    :param arr: The list needs to be sorted
    :return: A sorted list
    """
    # Find the maximum number of digits in the list
    max_digits = max([len(str(x)) for x in arr])

    # Set the base (radix) to 10
    base = 10

    # Create a list of buckets to store the digits
    buckets = [[] for _ in range(base)]

    # Iterate through each digit, starting with the least significant
    for i in range(0, max_digits):
        # Iterate through the elements in the list
        for x in arr:
            # Extract the i-th digit from the element
            # (starting from the rightest digit)
            digit = (x // base ** i) % base
            # Add the element to the bin for the i-th digit
            buckets[digit].append(x)
        # Combine the buckets back into the list, starting with the elements in the 0 queue
        arr = [x for queue in buckets for x in queue]
        # Clear the buckets for the next iteration
        buckets = [[] for _ in range(base)]

    return arr


# Test the function
# print(radix_sort([38, 2, 100, 5, 276, 42]))

"""
merge sort: divide & conquer strategy
steps : 1) divide(keep partitioning by finding middle) until base case
        2) Recursively mergeSort(left), mergeSort(right) merge all parts.
        3) merge in temp. array
this is depth-first implementation. 
"""


def mergeSort(arr: list, si: int, ei: int):
    # base case
    if si >= ei:
        return
    # kaam
    mid = si + int((ei - si)/2)  # or (si + ei)/2
    mergeSort(arr, si, mid)  # left part
    mergeSort(arr, mid+1, ei)  # right part
    merge(arr, si, mid, ei)


def merge(arr, si: int, mid: int, ei: int):
    temp = [0] * int(ei - si + 1)
    i = si  # iterator for left part
    j = mid + 1  # iterator for right part
    k = 0  # iterator for temp array

    while i <= mid and j <= ei:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # for left over elements of 1st sorted left part
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # for left over elements of 2nd sorted right part
    while j <= ei:
        temp[k] = arr[j]
        j += 1
        k += 1

    #copy temp to original array
    l = si
    for k in range(len(temp)):
        arr[l] = temp[k]
        l += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge2(left, right)


def merge2(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result


# arr = [6, 3, 9, 5, 2, 8]
# mergeSort(arr, 0, len(arr)-1)
# print(arr)
# print(merge_sort(arr))


"""
quick sort: Pivot & Partition strategy (kid of d & c)
steps: 1) Pivot (last element)
       2) Partition (parts)
       3) quickSort(left), quickSort(right
"""


def quickSort(arr: list, si: int, ei: int):
    #base case
    if si >= ei:
        return
    #kaam last element
    pIdx = partition(arr, si, ei)
    quickSort(arr, si, pIdx-1)  #left
    quickSort(arr, pIdx+1, ei)  #right


def partition(arr: list, si: int, ei: int):
    pivot = arr[ei]
    i = si - 1  # to make place for els smaller than pivot
    for j in range(si, ei):
        if arr[j] <= pivot:
            i += 1
            #swap
            arr[j], arr[i] = arr[i], arr[j]
    # swap for pivot element
    i += 1
    arr[ei], arr[i] = arr[i], arr[ei]
    return i


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [6, 3, 9, 5, 2, 8, -5]
quickSort(arr, 0, len(arr)-1)
print(arr)
# print(quick_sort(arr))
