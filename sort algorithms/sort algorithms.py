"""when we have significant database, we do require sorting of data. ex, arranging client insurance due by date,
rank wise class performance, department wise employee sorting.
So it's an essential task.
Due to tunneling view of computer systems + comparison operator handles 2 values at a time, we need to design
sorting algorithm accordingly. Like humans, computer can't process multiple attributes at same time, like you can
easily find the shortest persons from 1 row in 1 look.
"""

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


# sample_array = [1, 34, 456, 2, 4545, 7]
# sorted_array = bubble_sort(sample_array)
# print(sorted_array)

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
        print("for this iteration pointer and smallest_value_index was ", i, pointer_at_smallest_value)
        array[i], array[pointer_at_smallest_value] = array[pointer_at_smallest_value], array[i]
    return array


sample_array = [34, 12, 1, 56, 8, 78, 2, 8, 890]
# sample_array = [6]
sorted_array = selection_sort(sample_array)
print(sorted_array)
