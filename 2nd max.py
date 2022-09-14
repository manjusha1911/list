# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers.sort()
# print(numbers)
# print(numbers[-2])
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
sec_max=0
while i<len(numbers):
    n=numbers[i]
    if n>max :
        max=n
    elif sec_max<max and n>sec_max:
        sec_max=n
    i+=1
print(sec_max)









