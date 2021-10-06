import random
# 06 Практикум. Игра Угадай число
# Первый вариант. Простой
secret_number = random.randint(1, 100)
print(secret_number)
while True:
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == secret_number:
        print('Вы угадали!')
        break
    elif secret_number < user_number:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')

