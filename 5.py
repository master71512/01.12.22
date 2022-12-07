# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

path1 = 'D:/GB/Python/HW/01.12.22/1.txt'
path2 = 'D:/GB/Python/HW/01.12.22/2.txt'
data1, data2 = open(path1, 'r'), open(path2, 'r')
string1, string2 = data1.read(), data2.read()
data1.close()
data2.close()

res = []
def spliter (string):
    result = []
    while string != '':
        current_coef = 0
        current_pow = 0
        current_index = string.find('*x^')
        if current_index == -1:
            current_index = string.find('*x')
            if current_index == -1:
                for i in string:
                    if i.isdigit():
                        current_coef = 10*current_coef + int(i)
                current_pow = 0
                string = ''
            else: 
                current_coef = int(string[:current_index])
                string = string[current_index + 2:]
                current_pow = 1
        else:
            current_coef = int(string[:current_index])
            string = string[current_index + 3:]
            current_index = string.find(' ')
            current_pow = int(string[:current_index])
            string = string[current_index + 3:]
        result.append((current_pow, current_coef))
    return result

res1 = spliter(string1)
res2 = spliter(string2)
len_res1 = len(res1)
len_res2 = len(res2)

def SumCoef(x, y, list1, list2):
    result = []
    for i in range(x):
        flag = False
        for j in range(y):
            if list1[i][0] == list2[j][0]:
                flag = True
                result.append((list1[i][0], list1[i][1] + list2[j][1]))
        if not flag:
            result.append(list1[i])
    for j in range(y):
        flag = False
        for i in range(x):
            if list2[j][0] == list1[i][0]:
                flag = True
        if not flag:
            result.append(list2[j])
    return result

if len_res1 > len_res2:
    result_coef = SumCoef(len_res1, len_res2, res1, res2)
else:
    result_coef = SumCoef(len_res2, len_res1, res2, res1)
result_coef.sort(reverse=True)
result_string = ''
for i in range(len(result_coef)):
    current_pow = result_coef[i][0]
    result_string += str(result_coef[i][1])
    if current_pow > 1:
        result_string += '*x^' + str(current_pow)
    elif current_pow == 1:
        result_string += '*x'
    if i < len(result_coef) - 1:
        result_string += ' + '
data = open('1.txt', 'a')
data.write(result_string + '\n')
data.close()