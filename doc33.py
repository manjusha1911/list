a=[12,67,98,34]
i=0
z=[]
while i<len(a):
    b=a[i]
    j=0
    x=str(b)
    sum=0
    while j<len(x):
        y=int(x[j])
        sum=sum+int(y)
        j+=1
    z.append(sum)
    i+=1
print(z)