def bubble_sort(nums):    
    for _ in range(len(nums)):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    print(nums)

# example usage:
nums = [8, 4, 3, 1, 7, 9, 6, 5, 2]
bubble_sort(nums)
