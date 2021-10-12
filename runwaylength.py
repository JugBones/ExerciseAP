#formula
v = eval(input("Enter speed in m/s: "))
a = eval(input("Enter acceleration in m/s**2: "))
l = (v**2)/(2*a)

#result
print("The minimum runway length for the airplane is: {:.4f} m.".format(l))
