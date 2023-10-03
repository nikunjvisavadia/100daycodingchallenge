num=int(input())
for i in range(0,num):
    feed=input()
    if ("010" or "101") in feed:
        print("Good")
    else:
        print("Bad")