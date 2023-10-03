for _ in range(int(input())):
    a= set(input())
    b= set(input())
    ans= False
    al= len(a)
    bl= len(b)
    if(al<bl):
        for e in a:
            if(e in b):
            ans= True
            break
    else:
        for e in b:
            if(e in a):
            ans= True
            break
    if(ans):
        print("Yes")
    else:
        print("No")