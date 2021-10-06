import random
# 06 Практикум. Игра Угадай число
# игра для разных пользователей (многопользовательская)
secret_number = random.randint(1, 100)
print(secret_number)
user_number = None
count_user = 0
# добавляем выбор уровня сложности (попыток угадывания)
choice_level = int(input('Выбирите уровень сложности от 1 до 3-х: '))
levels = {1: 7, 2: 4, 3: 3}
print(f'Вам дается {levels[choice_level]} попытки')
max_count_user = levels[choice_level]
# количество пользователей
user_count = int(input('Введите количество пользователей: '))
# организация списка количества игроков
user_play = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ')
    user_play.append(user_name)
# определяем имя победителя
is_winner = False
winner_mane = None
# ЦИКЛ ИГРЫ
# Логика: пока не определен правильно угадавший...
while not is_winner:
    # игра идет в пределах выбранного кол-ва попыток
    count_user += 1
    if count_user > max_count_user:
        print(f'Вы использовали количество попыток ({max_count_user} раз). Для всех игра окончена.')
        break
    # Пока в диапазоне выбранного кол-ва попыток, игра продолжается
    print(f'Попытка № {count_user}')
    # для такого-то игрока....
    for i in user_play:
        # вывод имени игрока
        print(f'Ход пользователя: {i}')
        user_number = int(input('Введите число от 1 до 100: '))
        # Если такой-то игрок угадал...
        if user_number == secret_number:
            is_winner = True
            winner_mane = user_name
            # выход из цикла
            break
        # Если не угадал, то тгра продолжается...
        elif secret_number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
# Объявление имени победившего
else:
    print(f'{winner_mane} Вы угадали!')
