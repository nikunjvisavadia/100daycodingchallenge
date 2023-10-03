word = input('Enter the string :')
freq = 0
for i in range(0,len(word)):
    char = word[i]
    freq = word.count(char)
    print(str(freq) + ' is the frequency of '+char)