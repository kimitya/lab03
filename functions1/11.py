def palidr(a):
    reversestring=""
    for i in range(len(a)-1, -1, -1):
        reversestring += a[i]
    if reversestring==a:
        return True
    return False

a=input()
print(palidr(a))