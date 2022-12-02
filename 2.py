# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('введите число: '))
nums = []
i = 2
while num > 1:
    if num % i == 0:
        flag = True
        j = 2
        while j <= i//2:
            if i % j == 0:
                flag = False
            j += 1
        if flag:
            nums.append(i)
            num = num // i
            i = 2
    else:
        i += 1    
print(nums)                
