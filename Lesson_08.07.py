# функции
# использование встроенных функций. Функция:  sorted
# создаем произвольный набор чисел
numbers = [1, 5, 3, 5, 9, 7, 11]
print(numbers)
# сортировка по возрастанию
print(sorted(numbers))
# сортировка по убыванию
print(sorted(numbers, reverse=True))
# набор строк
names = ['Max', 'Alex', 'Kate']
# сортировка по алфавиту
print(sorted(names))
print(sorted(names, reverse=True))
# города и численность населения (условно).
# Данные  в виде списка. Элементы списка - кортежи
cities = [('Москва', 1000), ('Tokyo', 3000), ('London', 500), ]
# сортировка городов по алфавиту
print(sorted(cities))
print(sorted(cities, reverse=True))
# сортировка городов по численности населения


def by_count(argument_people):
    return argument_people[1]


# сортировка идет по ключу "key" , но в значение ключа передается функция "by_count"
print(sorted(cities, key=by_count))
# тот же результат, но с использованием  lambda-функции (в значение ключа передается lambda-функция)
print(sorted(cities, key=lambda argument: argument[1]))


