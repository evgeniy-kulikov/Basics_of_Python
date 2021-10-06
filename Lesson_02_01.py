# Объявление переменной
# имя_переменной = значение переменной
person_name = 'Макс'
age = 30
period = 3.2
is_good = True
person = None
print(type(person_name))
print(type(age))
print(type(is_good))
print(type(person))

# Приведение типов переменных:
# число к строке str(number)
# Строка к числу int (world)
birthday_year = '1964'
period = 57
age = int(birthday_year) + period
print(age)
# конкатенация строк
print(birthday_year + str(period))
# использование сепаратора (sep=) при выводе строки (разделитель слов)
print(person_name, age)
print(person_name, age, sep=': ')
# использование разделителя строк (end=)
print('Использование разделителя строк (end=)')
# разделитель(end=) вместо переода на новую строку добавляет следующую сторку к предыдущей
print(person_name, age, end='***')
# если end='\n' то он добавляет переход на новую строку
print(person_name, age, end='\n')
print(1, end='\n')
print(2, end='\n')
# Вввод данных input()
print('Вввод данных input()')
name = input('Ваше имя: ')
print('Привет, ', name)
# функция input() вводит только тип данных СТРОКА
name = input('Ваше имя: ')
print(type(name))
age = input('Ваш возраст: ')
print(type(age))
# В ряде случаев поэтому, необходимо преобразовать строку в число
print('преобразовать строку в число')
age = int(input('Ваш возраст: '))
period = 15
print('Через 15 лет Вам будет: ', age + period)



