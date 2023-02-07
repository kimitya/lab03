def histogram(num):
    for i in num:
        for j in range(i):
            print("*", end='')
        print()
        
histogram([4, 9, 7])