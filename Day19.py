num = input("Enter a number : ")
new=int(num)
arm=len(num)
sum=0

for i in range (0,new):
    last=new%10
    sum=sum+(last**arm)
    new=new//10

if sum == int(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
