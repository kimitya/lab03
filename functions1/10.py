def uniqlist(list1):
    newlist=[]
    for i in list1:
        if i not in newlist:
            newlist.append(i)
    return newlist

a = [i for i in input().split()]
print(uniqlist(a))
    