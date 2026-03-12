#using slicing(simplest)
text=input("Enter string:")
rev=text[::-1]
print("reversed string:",rev)




#using a basic loop
text=input("Enter a string:")
rev=""
for ch in text:
    rev=ch+rev
print("reversed string:",rev)




#using reversed() function
text=input("Enter a string:")
rev="".join(reversed(text))
print("reversed string:",rev)