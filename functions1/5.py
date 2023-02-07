from itertools import permutations 

def Permut(a):
    perm = permutations(a) 
    for i in list(perm):
        for j in i:
            print(j, end='')
        print()
    

s = 'abcd'
a = ([i for i in s])

Permut(a)

# abc -> bac, cba, acb,    

        
  