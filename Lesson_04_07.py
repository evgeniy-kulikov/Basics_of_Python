print('* * * * * * использование функции  range  * * * * * * ')
# пример списка  победителей winners
winners = ['Max', 'Leo', 'Kate']
# перебор с использованием for
for i in winners:
    print(i)
# пример использования функции  range
numbers = range(10)
print(numbers)
print(type(numbers))
# _____ <class 'range'> - это тип 'диапазон' _____
# выводим список диапазона  range
print(list(numbers))
# возвращаемся к примеру списка  победителей winners
print(len(winners))
# 3
print(range(len(winners)))
# range(0, 3)
for i in range(len(winners)):
    print('индекс: ', i)
    print('элемент: ', winners[i])
# улучшение примера вывода списка победителей  winners
# i+1  - уходим от нулевого места
for i in range(len(winners)):
    print(i+1, ') ', winners[i])
# вывод последовательности 10 чисел (начинается с нуля)
print(list(range(10)))
# вывод последовательности 9 чисел (от 1 до 9)
print(list(range(1, 10)))
# вывод последовательности нечетных чисел (от 1 до 9)
print(list(range(1, 10, 2)))
# range(start, end, step)
# вывод последовательности нечетных чисел (от 1 до 9) через цикл " for " в столбец
for numbers in range(1, 10, 2):
    print(numbers)
# модификация примера вывода списка победителей  winners с использованием  range
# другими словами  это -  for i in range(1, 4):
for i in range(1, len(winners)+1):
    print(i, ') ', winners[i-1])
