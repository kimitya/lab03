from  random import randint

name = input("Hello! What is your name?\n")
print()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

a = randint(1, 20)
t = False
cnt=1
while t!=True:
    print("Take a guess.")
    b = int(input())
    if a==b:
        print()
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    else:
        cnt += 1
        print()
        if b>a:
            print ("Your guess is too high.")
        else:
            print("Your guess is too low.")
            

    
    