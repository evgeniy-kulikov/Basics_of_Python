# n = int(input(''))  # школник
# k = int(input(''))  # мандарин
# c = k // n  # каждому
# b = k - (c * n)  # остаток
# print(c)  # каждому
# print(b)  # остаток

# Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
# abc, acb, bac, bca, cab, cba
n = int(input(''))
a = str(n // 100)
b = str((n // 10) % 10)
c = str(n % 10)
print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')
