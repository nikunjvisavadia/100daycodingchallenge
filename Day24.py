rows=int(input("Enter the number of rows: "))
for i in range(0,rows+1):
    for j in range(i,rows):
        print(" ",end="")
    for k in range(0,2*(i-1)+1):
        print("*",end="")
    print("\r")
print()