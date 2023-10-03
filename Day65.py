t=int(input())
for A in range(t):
    n,b=map(int,input().split(" "))
    dict={}
    for x in range(n):
        w,h,i=map(int,input().split(" "))
        dict[w*h]=i
    dd=sorted(dict)
for x in range(len(dd)-1,-1,-1):
    m=dict[dd[x]]
    if m<=b:
        print(dd[x])
        break
    else:
        print("no tablet")