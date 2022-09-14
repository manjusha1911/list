list=[11,13,44,55,34.67,12,-94.89,'pyton',0,'c#']
b=[]
i=0
while i<len(list):
    n=list[i]
    if type(n)==int:
        b.append(n)
    i+=1
print(b)
 