# Вычислить число Pi c заданной точностью d, не используя ф. round()

from math import pi

d = float(input('введите d: 10^(-1) ≤ d ≤10^(-10)\n'))
k = 0
while d < 1:
    d *= 10
    k += 1
res = int(pi * (10**(k+1)))
if res % 10 >= 5:
    res = (res // 10 + 1)*(10**(-k))
else:
    res = res // 10 * (10**(-k))
print(res)
