# Математические операции
# //  - целая часть от деления
print('//  - целая часть от деления 25/8')
print(25//8)
# %  - остаток от деления
print('%  - остаток от деления 25/3')
print(25 % 8)
# **  - возведение в степень
print('**  - возведение в степень 25 в кубе')
print(25**3)
#
# Логические операции
print('Логические операции')
old_live = 85  # средняя продолжительность жизни
age = int(input('Сколько Вам лет?: '))
print('Ваш возраст равен средней продолжительности жизни: ', age == old_live)
print('Ваш возраст НЕ равен средней продолжительности жизни: ', age != old_live)
print('Ваш возраст больше или равен средней продолжительности жизни: ', age >= old_live)
print('Ваш возраст меньше или равен средней продолжительности жизни: ', age <= old_live)
print('У Вас юбилей: ', age % 5 == 0)
#
# Сложные логические выражения
# Операторы:  and  or   not
print('Операторы:  and  or   not')
age = int(input('Сколько Вам лет?: '))
print('Ваш возраст равен средней продолжительности жизни: ', not age != old_live)
print('У Вас юбилей И ваш возраст меньше средней продолжительности жизни', age % 5 == 0 and age < old_live)
#
# Оператор:   if, elif,  else
print('Оператор:   if, elif,  else')
age = int(input('Введите свой возраст: '))
if age < 18:
    print('Доступ закрыт!')
elif age >= 65:
    print('Вам пора за пенсией')
else:
    print('Доступ разрешен')
    if age % 5 == 0:
        print('Ого, у Вас юбилей!')
print('Конец программы')
#
# Угадай число
print('Прграмма "Угадай число"')
secret_number = 23
your_value = int(input('Введите свое число от 1 до 100: '))
if your_value == secret_number:
    print('Вы угадали!')
else:
    if your_value > secret_number:
        print('Нужно меньше')
    elif your_value < secret_number:
        print('Нужно меньше')
print('Конец программы')

