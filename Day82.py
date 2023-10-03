test=int(input())
for _ in range(test):
    n=int(input())
    ls=[]
    for _ in range(n):
        ls.append(int(input(),2))
    mx=len(str("{0:b}".format(max(ls))))
    for i in range((2**mx)-1,min(ls),-1):
        if i not in ls:
            print("{0:b}".format(i))
            break