"""non-overlapping = disjoint"""

"""
You are given n activites with thier start and end times. Select the maxium number of activities
that can be performed by a single person, assuming that a person can only work on a single
activity at a time. Activies are sorted according to end time.

Approach:
    1) End time basis sort is sensible as if we sort on start time, it may eat up full time.
    2) Pick 1st activity after sort. A0 
    3) start time >= last chosen activity end time:
            count ++ 
"""

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]


def greedyOnSorted():
    # end time basis sort
    maxAct = 0
    selectedAct = []

    # 1st activity
    maxAct = maxAct + 1
    selectedAct.append(0)
    lastEnd = end[0]
    for i in range(1, len(end)):
        if start[i] >= lastEnd:
            # activity select
            maxAct += 1
            selectedAct.append(i)
            lastEnd = end[i]

    print("max activities = ", maxAct)
    for i in selectedAct:
        print("A"+str(i), end="\t")


"""
Now what if end times are not sorted ? So we can sort it with tagging it's original index to show
list of selected activities from original index. 
So, 2D list can can be useful to sort end time with original index & start time.
"""

unsortedEnd = [2, 4, 6, 7, 9, 9]


def greedyOnUnSorted():
    sortedEnd = [[i, start[i], end[i]] for i in range(len(end))]
    sortedEnd.sort(key=lambda x: x[2])

    # consider 1st activity from sorted end time
    maxAct = 1
    selectedAct = [sortedEnd[0]]
    lastEnd = sortedEnd[0][2]

    for i in range(len(sortedEnd)):
        if start[i] >= lastEnd:
            maxAct += 1
            selectedAct.append(sortedEnd[i])
            lastEnd = sortedEnd[i][2]

    print("max activities = ", maxAct)
    for i in selectedAct:
        print("A"+str(i[0]), end="\t")


greedyOnUnSorted()

"""
tc for sorted would be O(n)
tc for unsorted would be O(n*logn)
"""