from math import sqrt
a = int(input("please enter first side of a triangle: "))
b = int(input("please enter second side of a triangle: "))
c = int(input("please enter third side of a triangle: "))


perimeter = a + b + c
p = perimeter / 2
area = sqrt(p * (p - a) * (p - b) * (p - c))
print("perimeter is: ",perimeter)
print("area is: ", area)
