def two_sum_optimized(nums, target):
    num_indices = {}
    n = len(nums)
    for i in range (n):
        search = target - nums[i]
        if search in num_indices:
            return [num_indices[search], i]
        else:
            num_indices[nums[i]] = i

    return None


myArray = [1, 4, 21, 24, 7, 8]
target_sum = 28
result  = two_sum_optimized(myArray, target_sum)

if result:
    print(f'Two numbers at indices {result[0]} and {result[1]} add up to the target sum.')
else:
    print('No such pair found.')