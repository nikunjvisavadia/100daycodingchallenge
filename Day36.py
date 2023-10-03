word= input("Enter a String : ")
word=word[0:1].upper()+word[1:len(word)-1]+word[-1].upper()
print(word)