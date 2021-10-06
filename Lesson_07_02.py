# Вариант игры PC c пользователем от преподавателя
import random
min_number = 1
max_number = 100
# для того что бы зайти в цикл result делаем пустым
result = None
# логика ЦИКЛА: пока result не равен '='
while result != '=':
    number = random.randint(min_number, max_number)
    print(number)
    result = input('"=" ">" "<" ')
    if result == '>':
        min_number = number + 1
    elif result == '<':
        max_number = number - 1
print('Число угадано!')
