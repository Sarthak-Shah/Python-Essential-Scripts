"""
it's a classical problem.
knapsack = bori = bag
it used to solved by greedy algorithm and 0-1 knapsack solved by dynamic programming.
"""

"""
Given the weights and values of N items, put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.

Approach:
    1) need to consider value/weight ratio to get maximum total value
    2) if capacity >= weight, add full item. 
            capacity = capacity - wt[i]
            val = val + val[i]
       else, add item with remaining weight. 
            val = val + (ratio * capacity)
            break
"""

value = [60, 120, 100]
weight = [10, 30, 20]
W = 50 # total capacity of knapsack


def fractionalKnapsack():
    # need to get ratio and arrange it in descending order to take first one
    # will take 2D array to tag its original index
    itemWithRatio = [[i, value[i]/weight[i], weight[i]] for i in range(len(weight))]
    print("this is item with ratio ", itemWithRatio)
    # now need to arrange it in descending order to take first with optimum value.
    itemWithRatio.sort(key=lambda x:x[1], reverse=True)
    print("this is sorted ratio ", itemWithRatio)

    capacity = W
    totalValue = 0
    for i in range(len(itemWithRatio)):
        if capacity >= itemWithRatio[i][2]:
            totalValue = totalValue + itemWithRatio[i][1]*itemWithRatio[i][2]
            capacity = capacity - itemWithRatio[i][2]
        else:
            totalValue = totalValue + (itemWithRatio[i][1]*capacity)
            break
    return totalValue


print(fractionalKnapsack())

"""
Time complexity (tc) would be O(nlogn)
here, linear comes from for loop with length
logn comes from sorting
"""
