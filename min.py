# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# min=1000
# while i<len(numbers):
#     n=numbers[i]
#     if n<min:
#         min=n
#     i+=1
# print(min)

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers.sort()
# print(numbers[-1])
# print(numbers[0])
i=0
min=numbers[i]
max=numbers[i]
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    elif numbers[i]<min:
        min=numbers[i]
    i+=1
print(max)
print(min)
