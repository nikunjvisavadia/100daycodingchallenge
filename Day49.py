n = int(input())
arr1 = []
arr2 = []
for i in range(0,n):
	temp = int(input())
	arr1.append(temp)

for i in range(0,n):
	temp = int(input())
	arr2.append(temp)

arr1.sort()
arr2.sort(reverse=True)
sum = 0

for i in range(0, n):
	sum = sum + (arr1[i] * arr2[i])

print("Minimum Scalar Product :",sum)