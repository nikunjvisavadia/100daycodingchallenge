def sm(ar):
    sum=0
    for i in ar:
        sum += i
    return sum

def sqr(no):
    no = (no*no)
    return no

num=int(input("Enter number of elements in the array :"))
ar=[]
for j in range(0,num):
    tmp=int(input())
    ar.append(sqr(tmp))
    
print(sm(ar))
    