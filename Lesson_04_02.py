# Урок 4.2
#  Форматирование строк
print('Форматирование строк')
name = 'Alex'
age = 25
# Конкатенация
hello_str = 'Привет ' + name + ' тебе ' + str(age) + ' лет'
print(hello_str)
# Оператор %   где %s строка а  %d число далее в скобках нужный порядок переменных
hello_str = 'Привет %s тебе %d лет' % (name, age)
print(hello_str)
# функция .format (рекомендуемый метод)
# тип переменных определяется автоматически
hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)
# пример
# из строки top_best делаем строку: Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом!
top_best_5 = 'Первые пять мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
print(top_best_5)
# находим нужный для отрезания первый и последний индекс в строке top_best
start = top_best_5.find('1')
# print('Значение start: ', str(start))
# Значение start:  35
end = top_best_5.find('4')
# print('Значение start: ', str(end))
# Значение end:  66
# для удаления лишнего пробела перед "4"
end -= 1
# делаем нужный вырез из строки
top_best_3 = top_best_5[start:end]
print(top_best_3)
# через функцию .format() вставляем выркзанную строку в другую новую
result_1 = 'Поздравляем {} с успехом!'.format(top_best_3)
print(result_1)
# добовляем функцию .upper() для перевода строчных букв а ЗАГЛАВНЫЕ
result_2 = 'Поздравляем {} с успехом!'.format(top_best_3.upper())
print(result_2)