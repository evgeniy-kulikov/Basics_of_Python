# Функции
# Встроенные функции

# Функця abs (находит модуль числа)
print(abs(7))
print(abs(-7))

# Функци min   max
numbers = [1, 6, -3, 15, -7, 0, 3, -9]
print(min(numbers))
print(max(numbers))

# Функци round
# в параметрах указывается число и разряд округления
print(round(3.1415926, 2))

# Функця sum
print(sum(numbers))
# Функця enumerate (работает с выбранной последовательностью и нумерует ее по порядку)
# в параметрах указывается выбранная последовательность и число, с которого она будет нумироваться
# в цикле перебираются две переменные: порядковые номера и выбранная последовательность
name = ['Max', 'Leo', 'Kate']
for i, name in enumerate(name, 1):
    print(i, name)

# Задача: из введеных пользователем трех чисел получить min, max и сумму
# создаем пстой контейнер, для заполнения его в цикле
numbers = []
for i in range(3):
    number = int(input(f'Введите {i+1} число: '))
    numbers.append(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# Создаем пользовательскую функцию


def print_sep():
    print('-' * 50)
print_sep()



