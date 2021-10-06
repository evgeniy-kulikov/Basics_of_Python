# Практическое задание
# Вариант практического задания от лектора
# 1 задание
while True:
    user_number = int(input('Введите целое число: '))
    if (user_number > 0) and (user_number < 10):
        print(user_number ** 2)
        break
    else:
        print("Неверно! Введите число от 1 до 9: ")
print('Конец программы')
print('_ _ _ _ _ _ _ _ _ _')
""" 2 задание """
name = (input('Введите Ваше имя: '))
surname = str(input('Введите Вашу фамилию: '))
age = int(input('Введите Ваше возраст: '))
weight = int(input('Введите Ваше вес: '))
if age <= 30 and (weight >= 50) and (weight < 120):
    print(name, surname, age, ', год,', weight, 'вес', '- хорошее состояние')
elif (age > 30) and (age < 40) and (weight < 50) and (weight > 120):
    print(name, surname, age, ', год,', weight, 'вес', '- следует занятся собой')
elif age > 40 and (weight < 50) and (weight > 120):
    print(name, surname, age, ', год,', weight, 'вес', '- нужен врачебный осмотр')
""" У лектора код не все случаи описывает"""
