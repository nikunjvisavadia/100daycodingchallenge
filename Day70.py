N = int(input())
arr=list(map(int, input(). strip(). split()))
for i in range(0, 1):
    last = arr[len(arr)-1];
    for j in range(len(arr)-1, -1, -1):
        arr[j] = arr[j-1];
    arr[0] = last;
print();
for i in range(0, len(arr)):
    print(arr[i],end=" ")