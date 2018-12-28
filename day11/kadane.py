# Sidebar: Kadane's algorithm for finding maximum subarray sum
# This is a very good simple intro into dynamic programming!
# Given array: [1, -2, 3, 5, -5]
# The maximum subarray sum is 8 ([3, 5])


def kadane(array):
    global_sum = local_sum = 0

    for item in array:
        local_sum = max(item, local_sum + item)

        if local_sum > global_sum:
            global_sum = local_sum

    return global_sum


arr = [1, -2, 3, 5, -5]
arr_2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print('kadane:', kadane(arr))
print('kadane:', kadane(arr_2))


def max_sum(array):
    max_sum = 0
    array_len = len(array)

    for i in range(array_len):
        for j in range(i, array_len):
            if i == j:
                curr_sum = array[i]
            else:
                curr_sum = curr_sum + array[j]

            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum


print('max_sum:', max_sum(arr))
print('max_sum:', max_sum(arr_2))
