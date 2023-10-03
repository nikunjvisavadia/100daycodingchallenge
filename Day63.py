for i in range (int(input())):
    w1,w2,x1,x2,M=map(int,input().split(" "))
    h=(w2-w1)
    s1=x1*M
    s2=x2*M
    if (h>=s1 and h<=s2):
        print("1")
    else:
        print("0")