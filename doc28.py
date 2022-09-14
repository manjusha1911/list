# list=[1,1,2,3,4,5,1,2]
# b=[]
# for i in list:
#     if i!=1:
#         b.append(i)
# print(b)

list=[1,1,2,3,4,5,1,2]
i=1
b=[]
while i<len(list):
    n=list[i]
    if n!=1:
        b.append(n)
    i+=1
print(b)