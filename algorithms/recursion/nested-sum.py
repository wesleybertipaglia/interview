def nested_sum(nums, index = 0, sum = 0):
    if index >= len(nums):
        return
    sum += nums[index]
    print(sum)
    nested_sum(nums, index+1, sum)

# example usage:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nested_sum(nums)