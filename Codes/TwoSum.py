def two_sum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# Example usage:
myArray = [1, 4, 21, 24, 7, 8]
target_sum = 28
result = two_sum_bruteforce(myArray, target_sum)

if result:
    print(f'Two numbers at indices {result[0]} and {result[1]} add up to the target sum.')
else:
    print('No such pair found.')






