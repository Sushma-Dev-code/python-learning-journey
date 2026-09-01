def longest_subarray(arr, k):
    prefix_sum = 0
    max_length = 0
    first_index = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If prefix_sum itself is K
        if prefix_sum == k:
            max_length = i + 1

        # Check if there is a previous prefix sum
        # such that current_sum - previous_sum = k
        if prefix_sum - k in first_index:
            length = i - first_index[prefix_sum - k]
            max_length = max(max_length, length)

        # Store only the first occurrence
        if prefix_sum not in first_index:
            first_index[prefix_sum] = i

    return max_length


arr = [10, 5, 2, 7, 1, 9]
k = 15

print(longest_subarray(arr, k))