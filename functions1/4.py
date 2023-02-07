def filter_prime(num):
    newlist=[]
    for i in num:
        cnt =0
        for j in range (2, i):
            if i%j==0:
                cnt +=1
        if cnt==0 and i>1:
            newlist.append(i)
        cnt=0
    return newlist

num = [int(i) for i in input().split()]

print(filter_prime(num))
            
            
                
            
    
    