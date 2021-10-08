# Практическое задание
# Мой вариант практического задания
""" 1 """
user_number = int(input('Введите целое число: '))
print(user_number + 2)
print('Конец программы')

""" 2 мой вариант """
user_number = int(input('Введите целое число: '))
while user_number <= 0 or user_number >= 10:
    print('Неверно! Введите число от 1 до 9: ')
    user_number = int(input('Введите целое число: '))
print(user_number**2)
print('Конец программы')

""" 3 мой вариант """
user_name = (input('Введите Ваше имя: '))
user_surname = str(input('Введите Вашу фамилию: '))
user_age = int(input('Введите Ваше возраст: '))
user_weight = int(input('Введите Ваше вес: '))
if user_age < 30 and (50 < user_weight < 120):
    print(user_name, user_surname, '- хорошее состояние')
elif (user_age >= 30 or user_age <= 40) and (user_weight < 50 or user_weight > 120):
    print(user_name, user_surname, '- следует занятся собой')
elif (user_age > 40) and (user_weight < 50 or user_weight > 120):
    print(user_name, user_surname, '- нужен врачебный осмотр')
else:
    print(user_name, user_surname, '- Вы в хорошей форме, но следите за собой!')
print('Конец программы')

