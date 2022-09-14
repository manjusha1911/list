a=[1,2,3,4,5,6,7,8,9,10]
i=0
sum=0
while i<len(a):
    n=a[i]
    if n%2!=0:
        sum=sum+n       
    i+=1
print(sum)
