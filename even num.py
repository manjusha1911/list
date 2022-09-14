a=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
while i<len(a):
    n=a[i]
    b.append(str(n))
    if n%2==0:
        print(n)
    i+=1


