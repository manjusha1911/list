list=[40,80,2,4,9,7,6,11,13,17,19]
sum=0
even_sum=0
odd_sum=0
i=0
b=[]
c=[]
while i<len(list):
    n=list[i]
    sum=sum+n
    avg=sum/len(list)
    if list[i]%2==0:
        s=list[i]
        b.append(s)
        even_sum=even_sum+s
        even_avg=even_sum/len(b)
    else:
        k=list[i]
        c.append(k)
        odd_sum=odd_sum+k
        odd_avg=odd_sum/len(c)
    i+=1
print("sum:",sum)
print("average:",avg)
print(b)
print("even sum:",even_sum)
print("even avg:",even_avg)
print(c)
print("odd sum:",odd_sum)
print("odd avg:",odd_avg)
