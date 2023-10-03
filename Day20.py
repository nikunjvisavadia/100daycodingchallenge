def factors(num):
    fact=[]
    for i in range(1,num+1):
        if num%i == 0:
            fact.append(i)
    return fact

num=int(input("Enter a Number : "))
# print(factors(num))

if len(factors(num)) >2:
    print(num, " is not a prime number")
else:
    print(num, " is a Prime number")