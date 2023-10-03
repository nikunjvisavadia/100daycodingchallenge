def handshake(num):
    sum=0
    for i in range(1,num):
       sum= sum + (num-i)
    return sum 

num = int(input("Enter number of people in room : "))
print(handshake(num))