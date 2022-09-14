a=[2,4,6,8]
i=0
b=[]
while i<len(a)-1:
    n=a[i+1]-a[i]
    b.append(n)
    i+=1
print(b)