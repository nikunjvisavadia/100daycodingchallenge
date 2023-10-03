word = input('Enter the string :')
freq = 0
new=""
for i in range(0,len(word)):
    char = word[i]
    freq = word.count(char)
    if freq==1:
        new=new+char+" "
        
print(new)