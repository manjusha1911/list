# 8,3,5


# a=[8,2,3,4,5,6]
# n=a[:5:2]
# print(sum(n))


a=[8,2,3,4,5,6]
i=0
sum=0
while i<len(a):
    if i%2==0:
        sum=sum+a[i]
    i+=1
print(sum)