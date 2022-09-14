# a=["hydrabad","bangalore","delhi","chennai","vizag"]
# b=a.copy()
# print(b)
# colorlist=["red","blue","black","white","yellow","pink"]
# b=colorlist.copy()
# print(b)
# a=int(input("enter the number:"))
# rem=0
# while a>0:
#     b=a%10
#     rem=(rem*10)+b
#     a=a//10
# print(rem,end=" ")

a=int(input("enter the number:"))
b=int(input("enter the number:"))
while a<b:
    a+=1
    if a%2==0:
        print(a)
    # a+=1