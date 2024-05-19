def count_to(target, current = 1):
    if current > target:
        return
    
    print(current)
    count_to(target, current+1)

# example usage:
count_to(10)