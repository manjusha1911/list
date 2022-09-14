a=[1234,122,1984,19372,100]
result=True
i=0
b=[]
x=str(a[0])
for i in a:
    n=str(i)
    if x[0]!=n[0]:
        result=False
        break
    else:
        continue
print(result)
    
