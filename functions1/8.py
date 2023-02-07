def spy_game(nums):
    cntzero=0
    a = False
    for i in nums:
        if i==0:
            cntzero +=1
        if i==7 and cntzero>=2:
            a= True
    print (a)

        

spy_game([1,2,4,0,0,7,5]) #--> True
spy_game([1,0,2,4,0,5,7]) #--> True
spy_game([1,7,2,0,4,5,0]) #--> False
spy_game([7,9,9,0,8,0,3,3,7])
