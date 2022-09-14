a=[[1,3],[0],[9,11],[13,15,17]]
i=0
max_l=0
min_l=10
while i<len(a):
    n=a[i]
    c=len(n)
    if c>max_l:
        max_l=c
        e=a[i]
    elif c<min_l:
        min_l=c
        f=a[i]
    i=i+1
print("list maximum is","(",max_l,",",e,")")
print("list maximum is","(",min_l,",",f,")")
    
    
    