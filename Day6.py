x = int(input())
y = int(input())

if(x < 0 and y <0):
    print("This point lies in Third Quadrant.")
elif(x<0 and y>0):
    print("This point lies in Second Quadrant.")
elif(x>0 and y>0):
    print("This point lies in First Quadrant.")
else:
    print("This point lies in Fourth Quadrant.")