num=int(input("Enter a no: "))
copy=num
sum=0
fact=1
while num!=0:
    fact=1
    a=num%10
    for i in range (1,a+1):
        fact = fact*i

    sum=sum+fact
    num=num//10
print(sum)

if(sum == copy):
    print("Strong Number")
else:
    print("Not a strong number")