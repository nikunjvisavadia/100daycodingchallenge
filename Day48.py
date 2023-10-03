def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

nom=int(input("Enter the size of array : "))
print("Enter the elements of array")
ar1=[]
for i in range(0,nom):
    tmp=int(input())
    ar1.append(tmp)

print(Remove(ar1))