list=[1,1,2,3,3,4]
unique=[]
for n in list:
    if n not in unique:
        unique.append(n)
print(unique)