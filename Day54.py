def areDisjoint(set1, set2, m, n):
    set1.sort()
    set2.sort()
 
    i = 0; j = 0
    while (i < m and j < n):
         
        if (set1[i] < set2[j]):
            i += 1
        elif (set2[j] < set1[i]):
            j += 1
        else: 
            return "Not Disjoint"
    return "Disjoint"
 
num1=int(input("Enter the number of elements in first array : "))
arr1=list(map(int,input().split(' ')))

num2=int(input("Enter the number of elements in second array : "))
arr2=list(map(int,input().split(' ')))

print(areDisjoint(arr1,arr2,num1,num2)) 