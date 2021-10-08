# 04.6
# Последовательности
# Цикл for in
"""ПОВТОРЕНИЕ"""
# Строка, список, кортеж
string_any = 'Max, Leo, Kate'
list_any = ['Max', 'Leo', 'Kate']
roles_any = ('Max', 'Leo', 'Kate')
# Типы данных
print(type(string_any))
print(type(list_any))
print(type(roles_any))
# Имеется индексация
print(string_any[1])
print(list_any[1])
print(roles_any[1])
# Можно делать срезы [start:end:step]
print(string_any[2:])
print(list_any[2:])
print(roles_any[2:])
# Можно определять длину
print(len(string_any))
print(len(list_any))
print(len(roles_any))
# применение " if "
if 'M' in string_any:
    print('Эта буква есть в имени друга')
if 'Max' in list_any:
    print('У меня есть данный друг')
if 'Kate' in roles_any:
    print('У меня есть данный друг')
# цикл while
# _ _ _ _ _ цикл while для строки _ _ _ _ _
i = 0
while i < len(string_any):
    name = string_any[i]
    print(name)
    i += 1
# _ _ _ _ _ цикл while для списка _ _ _ _ _
i = 0
while i < len(list_any):
    name = list_any[i]
    print(name)
    i += 1
# _ _ _ _ _ цикл while для кортежа _ _ _ _ _
i = 0
while i < len(roles_any):
    name = roles_any[i]
    print(name)
    i += 1
# цикл " for "
# _ _ _ _ _ цикл for для списка _ _ _ _ _
for name in string_any:
    print(name)
# _ _ _ _ _ цикл for для списка _ _ _ _ _
for name in list_any:
    print(name)
# _ _ _ _ _ цикл for для кортежа _ _ _ _ _
for name in roles_any:
    print(name)
# * * * * * * for vc while - различия * * * * * *
# преимущества стоит отдать циклу  "for"'
# особенно при переборе последовательности
# если не нужно манипулировать с счетчиком индекса и условием цикла
