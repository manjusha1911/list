# list=[4,5,5,5,,3,8]
list=[1,1,1,64,23,64,22,22,22]
b=[]
i=0
count=0
for i in list:
    n=list.count(i)
    if n>2:
        if b.count(i)==0:
            b.append(i)
print(b)