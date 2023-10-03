n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=a/(b*b)
    if(c<=18):
        print(1)
    elif(19<=c<=24):
        print(2)
    elif(25<=c<=29):
        print(3)
    elif(30<=c):
        print(4)