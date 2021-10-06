# Мой вариант игры PC c пользователем
import random
pc_number = random.randint(40, 60)
print('Загадайте число от 1 до 100. Начинаю его отгадывать.')
print(f'Это {pc_number} ?')
pc_number_min = 0
pc_number_max = 100


# определение числа выбираемого PC
def pc_choice(int_1, int_2):
    return round((int_1 + int_2) / 2)


while True:
    user_number = (input('Если я угадал, то введите "=",\nЕсли мое число меньше, то введите "<",'
                         '\nЕсли мое число больше, то введите ">" \nВаш ответ: '))
    if user_number == '=':
        print('Ура, победа!')
        break
    elif user_number == '>':
        pc_number_max = pc_number
        pc_number = pc_choice(pc_number_min, pc_number_max)
        print(pc_number)
    else:
        pc_number_min = pc_number
        pc_number = pc_choice(pc_number_min, pc_number_max)
        print(pc_number)
print('Игра завершена!')
