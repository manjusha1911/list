
# a=[50,40,23,1000,12,5,10,7,2]
a=[1,2,3,4,7,9,10]
i=0
min=a[i]
max=0
secondmax=0
thirdmax=0
while i<len(a):
    num=a[i]
    if num>max:
        max=num
    elif num>secondmax:
        secondmax=num
    elif num>thirdmax:
        thirdmax=num
    elif num<min:
        min=num
    i=i+1
print(max)
print(secondmax)
print(thirdmax)
print(min)