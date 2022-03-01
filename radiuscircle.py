import math

rad, length = input("Enter radius and length: ").split()
rad, length = [float(rad), float(length)]

def area_f(x):
    area = x * x * math.pi
    return area

def volume_f(y, z):
    volume = y * z
    return volume

area = area_f(rad)
volume = volume_f(area, length)

print("the area is: ", round(area, 2))
print("the volume is: ", round(volume, 2))