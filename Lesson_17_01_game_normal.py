# Lesson_17
# Практикум
# Добавить возможность развлечения в процессе работы с менеджером.
# Для этого добавить в менеджер запуск одной из игр:
# “угадай число” или “угадай число (наоборот)”
#
# функция “угадай число”

import random


def game_normal():
    min_num = 1
    max_num = 100
    result = None
    while result != '=':
        number = random.randint(min_num, max_num)
        print(number)
        result = input(' (число больше, меньше, равно вашему ? ) > = < ')
        if result == '>':
            min_num = number + 1
        elif result == '<':
            max_num = number - 1
    print('Победа!')


if __name__ == '__main__':
    game_normal()
