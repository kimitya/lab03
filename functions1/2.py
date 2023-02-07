def Temperature(f):
    c = (5 / 9) * (f - 32)
    return c

f = int(input("Temperature in Fahrenheit: "))
print(Temperature(f))