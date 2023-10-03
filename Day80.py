from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    b = Counter(nums)
    c = True
    for i in b:
        if b[i]%2==1:
        c = False
    if c:
    print("YES")
    else:
    print("NO")4