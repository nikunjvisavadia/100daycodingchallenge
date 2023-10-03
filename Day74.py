t=int(input())
while t!=0:
    m,n=map(int,input().split())
    if m%2==0 and n%2==0:
        print('0')
    elif m%2==0 and n%2==1:
        print(m)
    elif m%2==1 and n%2==0:
        print(n)
    else:
        print(m+n+-1)
    t-=1