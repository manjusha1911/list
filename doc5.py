# list=[1,2,2,5,8,4,4,8]
# b=[]
# for i in list:
#     if i not in b:
#         b.append(i)
# print(b)
a=[1,2,2,5,8,4,4,8]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)
