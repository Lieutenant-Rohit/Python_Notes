# from math import remainder
# import math
# friends = 5
# #** -> power of something
# friends = friends ** 2
# print(friends)
#
# #%-->Gives remainder
# rema = friends % 2
# print(rema)
#
# x= 3.14
# y= -4
# z= 5
# result = round(x)
# print(result)
# #Absolute function -> give the distance from 0
# result = abs(y)
# print(result)
#
#
#
# result = pow(z,3)
# print(result)
#
# result = max(y,z,x)
# print(result)
#
# result = min(y,z,x)
# print(result)
#
# print(math.pi)
#
# k= 25
# result = math.sqrt(k)
# print(result)
#
#

import math
# radius = float(input("What is the radius: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle with radius {radius} is {round(circumference,2)} cm")
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle with radius {radius} is {round(area,2)} cm^2")

a = float(input("Enter side a: "))
b= float(input("Enter side b: "))
c= math.sqrt(pow(a,2) + pow(b,2))
print(c)
