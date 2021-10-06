# функции
# использование встроенных функций. Функция:  filter
# создаем произвольный набор чисел (кортеж (tuple))
numbers = (1, 2, 4, 5, 7, 8, 10, 11)
print(numbers)
# создаем функцию "is_even"  для получения четных чисел из любой последовательности


def is_even(arg):
    return arg % 2 == 0


# другой вариант функции "is_even2"  для получения четных чисел из любой последовательности
def is_even2(arg):
    if(arg % 2) == 0:
        return True
    else:
        return False


result = filter(is_even, numbers)
print(list(result))
# вместо отдельной функции  "is_even"  используем lambda-функцию
print(list(filter(lambda arg: arg % 2 == 0, numbers)))
# создаем набор строк []  (имен)
names = ['Max', 'Leo', 'Kate']
# получить строки больше 3-х символов
print(list(filter(lambda name: len(name) > 3, names)))
#

