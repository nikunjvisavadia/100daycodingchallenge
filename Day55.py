num=int(input("Enter the number of elements in an array : "))

arr1=list(map(int,input().split(' ')))
arr2=list(map(int,input().split(' ')))

arr1.sort()
arr2.sort()

product=0
for i in range(0,num):
    product += arr1[i]*arr2[i]

print(product)