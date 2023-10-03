n=int(input())
for test_case in range(0,n):
    str_len=int(input())
    str=input()
    res = [str[i: j] for i in range(len(str))
          for j in range(i + 1, len(str) + 1)]
    count=0
    print(res)
    for i in res:
        for j in range(1,len(res)):
            if i==res[j]:
                count =count+1
    print(count)