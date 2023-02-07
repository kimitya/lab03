def revstring(a):
    reversestring=""
    for i in range(len(a)-1, -1, -1):
        reversestring += a[i]
    return reversestring

a=input()
print(revstring(a))