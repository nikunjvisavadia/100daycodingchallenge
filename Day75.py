for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    if x % y == 0:
        print(x//y)
    else:
        print("-1")