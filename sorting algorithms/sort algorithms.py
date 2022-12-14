"""when we have significant database, we do require sorting of data. ex, arranging client insurance due by date,
rank wise class performance, department wise employee sorting.
So it's an essential task.
Due to tunneling view of computer systems + comparison operator handles 2 values at a time, we need to design
sorting algorithm accordingly. Like humans, computer can't process multiple attributes at same time, like you can
easily find the shortest persons from 1 row in 1 look.
"""
import time
# Bubble sort
"""
Like name, heavy elements will bubbled up after each iteration.
time complexity = inerloop elements(n-1) * outerloop elements = n * n = n^2 (ignoring -1)
"""


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


# sample_array = [3, 234, 42, 55, 2]*500
# start = time.time()
# sorted_array = bubble_sort(sample_array)
# end = time.time()
# print(f"Bubble Sort took : {end-start} for {sorted_array}")


# Selection sort
"""
Like name, here we select smallest element and put it in leftmost position.
then again we hunt for second smallest element and put it in 2nd leftmost position.
==>> think about comparisons and no. of swaps per iteraton ....
here, as compared to bubble sort, we are applying 1 swap per inner loop iterations.
and what about comparisons ? N*(N-1)/2 . (same as bubble sort ? )
"""


def selection_sort(array:list):
    length = len(array)
    for i in range(length):
        pointer_at_smallest_value = i
        for j in range(i, length):
            if array[pointer_at_smallest_value] > array[j]:
                pointer_at_smallest_value = j
        # print("for this iteration pointer and smallest_value_index was ", i, pointer_at_smallest_value)
        array[i], array[pointer_at_smallest_value] = array[pointer_at_smallest_value], array[i]
    return array


# sample_array = [3, 234, 42, 55, 2]*500
# # sample_array = [6]
# start = time.time()
# sorted_array = selection_sort(sample_array)
# end = time.time()
# print(f"Selection Sort took : {end-start} for {sorted_array}")


"""
insertion sort:
from 1st element, we keep adding 1 element from RHS and sorting LHS after adding each element.
It's still faster than selection and bubble sorting.
time complexity:
"""


def insertion_sort(array:list):
    sorted_array = []
    for i in range(len(array)):
        if i == 0:
            sorted_array.append(array[i])
        else:
            new_insertion = array[i]
            sorted_array.append(new_insertion)
            for j in range(len(sorted_array)-1,1,-1):
                if sorted_array[j] < sorted_array[j-1]:
                    sorted_array[j], sorted_array[j-1] = sorted_array[j-1], sorted_array[j]
    return sorted_array


def optimized_insetion_sort(arr:list):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return  arr


# start = time.time()
# sample_array = [3, 234, 42, 55, 2]*500
# # sorted_array = insertion_sort([1, 2, 4, 55, 3]*500)
# sorted_array = optimized_insetion_sort(sample_array)
# end = time.time()
# print(f"Insertion Sort took : {end-start} for {sorted_array}")
