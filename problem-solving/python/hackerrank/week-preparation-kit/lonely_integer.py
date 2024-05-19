def lonely_integer(nums):
    nums_set = set()
    
    for num in nums:
        if num in nums_set:
            nums_set.remove(num)
        else:
            nums_set.add(num)
    
    if len(nums_set) == 1:
        return nums_set.pop()
    else:
        raise ValueError("There is no unique number.")