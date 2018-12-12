# Sidebar: Kadane's algorithm for finding maximum subarray sum
# This is a very good simple intro into dynamic programming!
# Given array: [1, -2, 3, 5, -5]
# The maximum subarray sum is 8 ([3, 5])


def kadane(arr):
    start = end = global_sum = curr_sum = 0

    for index, k in enumerate(arr):
        curr_sum = max(k, curr_sum + k)

        if k == curr_sum:
            start = index

        if curr_sum > global_sum:
            global_sum = curr_sum
            end = index

    return arr[start:end+1]


print(kadane([1, -2, 3, -2, 4]))
