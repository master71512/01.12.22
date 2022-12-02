
num = int(input('введите число: '))
nums = []
i = 2
while num > 1:
    if num % i == 0:
        flag = True
        for j in range(2, i+1):
            if i % j == 0 and j != i:
                flag = False
        if flag:
            nums.append(i)
            num = num // i
            i = 2
    else:
        i += 1    
print(nums)                