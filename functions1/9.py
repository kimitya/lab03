from math import pi

def Volume(a):
    volume= ((4/3)*pi)*a**3
    print (volume)

radius = int(input("sphere radius: "))
Volume(radius)
