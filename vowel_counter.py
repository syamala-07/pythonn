text = input("Enter a sentence: ")
vowels = "aeiou"
count = {}
for ch in text:
    if ch in vowels:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
print(count)