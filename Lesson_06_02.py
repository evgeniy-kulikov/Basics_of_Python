import random
# 06 Практикум. Игра Угадай число
# Однопользовательская игра
secret_number = random.randint(1, 100)
print(secret_number)
user_number = None
count_user = 0
# добавляем выбор уровня сложности (попыток угадывания)
choice_user = int(input('Выбирите уровень сложности от 1 до 3-х: '))
levels_user = {1: 10, 2: 7, 3: 5}
max_count_user = levels_user[choice_user]
# цикл игры
while user_number != secret_number:
    count_user += 1
    if count_user > max_count_user:
        print(f'Вы использовали количество попыток ({max_count_user} раз). Игра окончена.')
        break
    print(f'Попытка № {count_user}')
    user_number = int(input('Введите число от 1 до 100: '))
    if secret_number < user_number:
        print('Ваше число больше загаданного')
    elif secret_number > user_number:
        print('Ваше число меньше загаданного')
else:
    print('Вы угадали!')
