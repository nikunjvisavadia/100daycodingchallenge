def gold(n,x,y):
    n=n+1
    pro=n*y
    if pro>=x:
        return "YES"
    else:
        return "NO"
    
num=int(input())
for i in range(0,num):
    num_player,total_cap,person_cap=list(map(int,input().split(' ')))
    print(gold(num_player,total_cap,person_cap))