def insert(string_s, insert_s, pos_i=0):
    return string_s[:pos_i] + insert_s + string_s[pos_i:]
q = int(input())
s = ''
for _ in range(q):
    query = input().split()
    c = query[0]
    i = int(query[1])
    if c == '+':
        sub = query[2]
        if i == 0:
            s = sub + s
        else:
            s = insert(s,sub,i)
    else:
        l = int(query[2])
        print(s[i-1:i+l-1])