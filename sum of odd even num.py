a=[1,2,3,4,5,6,7,8,9,10]
i=0
even_sum=0
odd_sum=0
while i<len(a):
    n=a[i]
    if n%2==0:
        even_sum=even_sum+n
    elif n%2!=0:
        odd_sum=odd_sum+n
    i=i+1
print("sum of even number:",even_sum)
print("sum of odd number:",odd_sum)