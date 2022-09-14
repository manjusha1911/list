# a= [1, 0, 0, 1, 1, 0, 1, 1]
# p=0
# i=-1
# s=0
# while i>=(-len(a)):
#     b=a[i]*2**p
#     s+=b
#     p+=1
#     i-=1
# print(s)



# b_num = list(input("Input a binary number: "))
# value = 0
# for i in range(len(b_num)):
#     digit = b_num.pop()
#     if digit =='1':
#         value = value + pow(2, i)
# print("The decimal value of the number is", value)

# a = [1, 0, 0, 2, 1]
# p=0
# i=-1
# s=0
# while i>=(-len(a)):
#     b=a[i]*2**p
#     s+=b
#     p+=1
#     i-=1
# print(s)

a= [1,0,0,"1", 1]
p=0
i=-1
s=0
while i>=(-len(a)):
    b=int(a[i])*2**p
    s+=b
    p+=1
    i-=1
print(s)




