# Циклы
print('Цикл  while')

# Угадай число с циклом   while
print('Прграмма "Угадай число"')
secret_number = 23
your_value = int(input('Введите свое число от 1 до 100: '))
while your_value != secret_number:
    if your_value > secret_number:
        print('Не угадали! Нужно меньше')
    elif your_value < secret_number:
        print('Не угадали! Нужно больше')
    print('Следующая попытка: ')
    your_value = int(input('Введите свое число от 1 до 100: '))
print('Вы угадали!')
print('Конец программы')

# Угадай число с циклом   while и командой break
print('Прграмма "Угадай число" с циклом   while и командой break')
secret_number = None
while True:
    your_value = int(input('Введите свое число от 1 до 50: '))
    if your_value == 23:
        break
    print('Не угадали! Следующая попытка: ')
print('Вы угадали!')
print('Конец программы')

"""Команда  Continue"""
print('Команда Continue')
print('Команды в цикле после Continue не выполняются')
"""Вывод нечетных чисел с использованием цикла while"""
number = 0
your_number = int(input('Введите любое число от 1 до 50: '))
while number <= your_number:
    if number % 2 != 0:
        print(number)
    number += 1
print('Конец программы')

"""Вывод нечетных чисел с использованием команды continue"""
print('Вывод нечетных чисел с использованием команды continue')
number = 0
your_number = int(input('Введите любое число от 1 до 50: '))
while number <= your_number:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1
print('Конец программы')

# while - else
print('Использование  else  в  теле цикла  while')
number = 0
while number <= 10:
    print(number)
    number +=1
else:
    print('Подчет окончен')
print('Конец программы')