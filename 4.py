# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал) многочлен степени k.
# Пример:
# k = 2  => 2*x² + 4*x + 5
# k = 3  => 41*x^3 + 6*x² + 2*x + 98

from random import randint

k = int(input('k = '))
string = ''
for i in range(k, -1, -1):
    temp = randint(0, 100)
    if temp > 0:
        if i < k:
            string += ' + '
        string += str(temp)
        if i > 1:
            string += '*x^' + str(i)
        elif i == 1:
            string += '*x'
data = open('1.txt', 'a')
data.write(string + '\n')
data.close()
