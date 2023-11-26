# Q3: Implement a Python function that, given an array of integers,
# finds the length of the longest subarray with a sum equal to a specified
# value K. Use a hash table to track cumulative sums efficiently.


def longest_subarray_with_sum(nums, K):
    sum_indices = {0: -1}
    max_length = 0
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num

        if (current_sum - K) in sum_indices:
            max_length = max(max_length, i - sum_indices[current_sum - K])

        if current_sum not in sum_indices:
            sum_indices[current_sum] = i

    return max_length


nums = [10, 5, 2, 7, 1, 9]
K = 15

result = longest_subarray_with_sum(nums, K)
print(f"The length of the longest subarray with sum {K} is: {result}")
