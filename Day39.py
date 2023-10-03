def ana(s1,s2):
    if sorted(s1)==sorted(s2):
        return "Anagram"
    else:
        return "Not an Anagram"
st1, st2 = input("Enter two values: ").split()
print(ana(st1,st2))