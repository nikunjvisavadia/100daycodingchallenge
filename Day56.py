def convert(a,n):
    for i in range (n):
        while (a[i]%2 == 0):
            a[i] = a[i]/2
        while (a[i]%3 == 0):
            a[i] = a[i]/3
    for i in range (n):
        if a[i] != a[0]:
            return False
    return True
n = int(input("Enter the number of elements in array "))
arr = []
print("Enter elements: ")
for i in range(n):
    arr.append(int(input()))
if convert(arr, n):
    print("Yes, possible")
else:
    print("No, it's not possible")