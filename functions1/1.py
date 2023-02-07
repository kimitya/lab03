def Ounces(grams: float):
    return 28.3495231 * grams

a = float(input("Grams: "))
print("In ounces:", Ounces(a))