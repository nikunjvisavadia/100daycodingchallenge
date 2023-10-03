def maxSubarrayProduct(arr, n):

	result = arr[0]

	for i in range(n):

		mul = arr[i]

		for j in range(i + 1, n):

			result = max(result, mul)
			mul *= arr[j]

		result = max(result, mul)

	return result

num=int(input("Enter the number of elements in an array : "))
arr=list(map(int,input().split(' ')))
n = len(arr)
print("Maximum Sub array product is", maxSubarrayProduct(arr, n))