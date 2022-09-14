# a=[1,2,3,4,3,3,2,3,4,1,6,5]
# b=list(set(a))
# print(b)
# a=[1,2,3,1,2,2]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
a=[1,2,3,1,2,2]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)
