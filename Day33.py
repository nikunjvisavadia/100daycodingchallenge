def palindrome(word):
    new=word[::-1]
    if new==word:
        return "Palindrome"
    else:
        return "Not a Palindrome"

word=input("Enter a String : ")
print(palindrome(word))