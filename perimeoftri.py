#formula
edge1 = float(input("Enter length of the edge 1: "))
edge2 = float(input("Enter length of the edge 2: "))
edge3 = float(input("Enter length of the edge 3: "))

if edge1+edge2 > edge3:
    if edge1+edge3 > edge2:
        if edge2+edge3 > edge1 :
            perimeter = edge1+edge2+edge3
            print("The perimeter is: ",perimeter)
else: 
    print("Perimeter cannot be calculated. Invalid input!")