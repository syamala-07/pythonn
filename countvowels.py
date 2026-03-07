text=input("Enter text:")
count=0
for i in text:
    if i in "aeiouAEIOU":
        count+=1
        print("vowels:",count)