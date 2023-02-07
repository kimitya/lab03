def Solve(numh, numl):
    rabbit = (numl-2*numh)/2
    chicken = numh-rabbit
    print(rabbit, chicken)
    
Solve(int(input()), int(input()))