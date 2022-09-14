# a=[1,1,2,3,4,4,5,1]
# b=[]
# i=0
# while i<len(a):
#     l=a[i]
#     x=a.count(1)
#     if x>0:
#         b.append(l)
#     print(b)
#     i+=1
#   o/p is not coming 
# a="abc"
# list(a)
# print(list(a))  
l=[2,8,9,6,4,10,12]
x=len(l)
b=[]
i=0
while i<x-1:
    b.append(l[i+1])
    i+=2
print(b)
   
    
    
    