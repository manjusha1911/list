list=[6,1,3,5,6,3,1]
b=[]
for i in list:
    if i not in b:
        b.append(i)
print(b)
p=1
for j in b:
    p=p*j
print(p)