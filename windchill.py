import math

ta = True
while(ta):
    temp = float(input("Please enter the temperature: "))
    if(-58<temp<41):
        ta = False
    else:
        print("please re-enter the Farenheit in the valid temperature: ")
    
v = True
while(v):
    spd = float(input("Enter the wind speed miles per hour : "))
    if(spd>=2):
        v = False
    else:
        print("Please re-enter the valid wind speed: ")

wci = 35.74 + 0.6215*ta - 35.75*math.pow(v,0.16) + 0.4275*ta*math.pow(v,0.16)

print("The windchill index is: {:.3f} ".format(wci))