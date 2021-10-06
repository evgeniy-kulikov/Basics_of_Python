# Lesson_14
# Генераторы списков
#
# В Python существует специальная синтаксическая конструкция, которая позволяет по определенным правилам
# создавать заполненные списки. Такие конструкции называются генераторами списков
#
# Применение:
# позволяет писать компактный и читаемый код
# вместо цикла for
# работают быстрее
#
# Синтаксис
# [ number for number in numbers if number > 0 ]

# Пример
# запмсать в список только положительные числа

numbers = [1, 2, 3, -4, 5, -1, - 2, -3]

# стандартный цикл
result = []
for i in numbers:
    if i > 0:
        result.append(i)
print(result)

# с использованием функции filter
result = []
# в функции filter два параметра (функция, итерируемый объект)
# lambda принимает i и возвращает i которые больше нуля
result = filter(lambda k: i > 0, numbers)
print(list(result))

# через генератор
# "for i in numbers" цикл который перебирает список чисел
# левая "i" переменная принимающая значения цикла
# "if i > 0" условие по которому записываем переменную в список
result = []
result = [i for i in numbers if i > 0]
print(result)
#
#
# Генераторы словарей
# есть список состоящий из кортежей
print('Генераторы словарей')
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, [5, 'not'])]
# стандартный цикл
result = {}
for i in pairs:  # в каждом кортеже
    key = i[0]
    val = i[1]
    result[key] = val  # в создаваемый словарь по ключу 'key' мы добавляем значение 'val'
print(result)
# через генератор словарей
result = {}
result = {i[0]: i[1] for i in pairs}  # 'i in pairs' это пары в цикле
print(result)
