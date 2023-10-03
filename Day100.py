from collections import Counter
for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=Counter(a)
    a=[]
    for k,v in b.items():
        a.append(v)
    if 4 in a:
        print("0")
    elif 3 in a:
        print("1")
    p=a.count(2)
    q=a.count(1)
    if p==2 or p==1 or q==4:
        print("2")