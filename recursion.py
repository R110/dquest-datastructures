# f = open('random_integers.txt', 'r')
# random_integers = [int(line) for line in f.readlines()]
lst= [2,12,3,5,16,6,17]

def merge(left_list, right_list):
    sorted = []
    while left_list and right_list:
        if left_list[0] < right_list[0]:
            sorted.append(left_list.pop(0))
        else:
            sorted.append(right_list.pop(0))
    sorted += left_list
    sorted += right_list
    return sorted

def merge_sort(unsorted, level=0):
    print("Unsorted: Level", level, unsorted)

    if len(unsorted) < 2:
        return unsorted
    midpoint = len(unsorted) // 2
    left_side = merge_sort(unsorted[:midpoint], level+1)
    #left and right side eq ual a single value(in a list) at deepest level
    right_side = merge_sort(unsorted[midpoint:], level+1)

    sorted = merge(left_side, right_side)
    print("Merge Sorted: Level", level, sorted)
    return sorted

random_sorted = merge_sort(lst)
print(random_sorted)

#log 2 N steps to get to base recursive case, * n merge (conquer) == O(nlog2n)



# -- = call to merge_sort()
# #1st call -- left side merge_sort()
# result = merge([2], [3,12]) == [2,3,12]

#         2 -- 2
# 2,12,3--
#               12 -- 12
#         12,3-- #2nd call --> merge([12],[3]) == [3,12]
#                3 -- 3
