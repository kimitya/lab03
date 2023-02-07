def has_33(nums):
    a = False
    for i in range(0, len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
           a = True 
           break
    print(a)

has_33([1, 3, 3]) # → True
has_33([1, 3, 1, 3]) # → False
has_33([3, 1, 3]) # → False