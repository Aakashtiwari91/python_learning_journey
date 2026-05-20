# return multiple values

# def circle_area_and_curcumrence(radius):
#     area = 3.14 * radius**2
#     circumfrence = 2*3.14*radius
#     return (area  , circumfrence)
# print(circle_area_and_curcumrence(2))


import math

def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2*math.pi*radius
    return area , circumference
a,c = circle_stats(2)
print("Area: ",round(a,2),"circumference: ",round(c,2))
