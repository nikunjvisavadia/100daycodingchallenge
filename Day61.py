def chess(a,b):
    if a+b<3:
        return 1
    elif 3<=a+b<=10:
        return 2
    elif 11<=a+b<=60:
        return 3
    else:
        return 4
        
num=int(input())
for i in range(0,num):
    c,d=list(map(int,input().split(' ')))
    print(chess(c,d))