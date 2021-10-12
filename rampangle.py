import math

g = 9.8
m = int(input("Enter the mass on the cart (in kg) : "))
f = int(input("Enter the force (in N) : "))

SinTh = f/m/g

Th = math.asin(SinTh)
Th = math.degrees(Th)

print("The angle of the ramp is : {:.1f} degrees.".format(Th))