for _ in range(int(input())):
    n,m = map(int,input().split())
    v = []
    for _m in range(m):
        x,y = map(int,input().split())
        v.append([y,x])
    v.sort()
    l = 0
    r = n - 1
    cnt = -1
    while(l <= r):
        mid = (l+r)//2
        seg = 1
        for i in range(m):
            if(seg >= v[i][0] or v[i][1] > seg):
                continue
            else:
                seg = min(seg + mid,v[i][0])
        if(seg == n):
            cnt = mid
            r = mid - 1
        else:
            l = mid + 1
    print(cnt)