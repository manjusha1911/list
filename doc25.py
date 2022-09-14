list=[4,6,4,3,3,4,3,4,3,6,6]
b=[]
i=0
for i in list:
    n=list.count(i)
    if n>0:
        if b.count(i)==0:
            b.append(i)
print(b)
 
 

     
    
